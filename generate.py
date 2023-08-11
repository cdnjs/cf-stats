"""
A script that generates the base MD stats report file, parses the stats Cloudflare provides
 and exports them to the DB as well as generating an MD table of them for the report.
"""
import calendar
import os
import re
import sqlite3
from random import choice, random
from typing import List, Dict, Union

import beautifultable
import requests


def generate_regex(order: List[str]) -> str:
    final = []
    patterns = {
        "requests": "\"?(?P<requests>\\d+)\"?",
        "resources": "\"?(?P<resource>[^\\s\"]+)\"?",
        "bandwidth": "\"?(?P<bandwidth>\\d+(?:\\.\\d+)?)\"?"
    }
    joiner = "[\\s|│,]*"
    for item in order:
        if item in patterns:
            final.append(patterns[item])
    final = "^" + joiner + joiner.join(final) + joiner + "$"
    return final


def parse_raw(url: str, column_regex: str) -> List[Dict[str, Union[int, float, str]]]:
    # Get the raw dump from the url
    raw = requests.get(url).text
    items = []
    file_regex = "^cdnjs\\.cloudflare\\.com\\/ajax\\/libs\\/(?P<library>.+?)\\/(?P<version>.+?)\\/(?P<file>.+)$"

    # Iterate over each line of the dump
    for line in raw.split("\n"):
        try:
            # Attempt to find the components through regex
            x = re.search(column_regex, line)
            y = x.groupdict()

            # Ensure correct datatypes
            y["requests"] = int(y["requests"])
            y["bandwidth"] = float(y["bandwidth"])

            # Parse resource further
            z = re.search(file_regex, y["resource"]).groupdict()
            for key, value in z.items():
                y[key] = value

            items.append(y)
        except:
            continue
    return items


def database_data(request_data: List[Dict[str, Union[int, float, str]]], month: int, year: int, total_data: dict):
    # Create db
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS DATA (resource text, bandwidth float, requests integer, library text, version text, file text, month integer, year integer)''')
    conn.commit()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS DATA_TOTALS (requests_1_percent integer, requests_3_days integer, bandwidth_1_percent float, bandwidth_3_days float, month integer, year integer)''')
    conn.commit()

    # Export all the data
    for row in request_data:
        c.execute(
            '''INSERT INTO DATA (resource,bandwidth,requests,library,version,file,month,year) VALUES (?,?,?,?,?,?,?,?)''',
            [
                row["resource"], row["bandwidth"], row["requests"], row["library"], row["version"], row["file"], month,
                year
            ])
    conn.commit()
    c.execute(
        '''INSERT INTO DATA_TOTALS (requests_1_percent,requests_3_days,bandwidth_1_percent,bandwidth_3_days,month,year) VALUES (?,?,?,?,?,?)''',
        [
            total_data["REQUESTS_1_PER"], total_data["REQUESTS_3_DAY"], total_data["BANDWIDTH_1_PER"],
            total_data["BANDWIDTH_3_DAY"], month, year
        ])
    conn.commit()

    # Create libraries view
    c.execute('''CREATE VIEW IF NOT EXISTS libraries AS
        SELECT
            *,
            total_requests / days AS requests_per_day,
            total_bandwidth / days AS bandwidth_per_day
        FROM
        (
            SELECT
                SUM(requests) * 100 AS total_requests,
                SUM(bandwidth) * 100 AS total_bandwidth,
                library,
                COUNT(DISTINCT(version || file)) AS files,
                COUNT(DISTINCT(version)) AS versions,
                year,
                month,
                (julianday(DATE(year || "-" || printf("%02d", month) || "-01", "+1 month")) - julianday(year || "-" || printf("%02d", month) || "-01")) AS days,
                year || "-" || printf("%02d", month) as date
            FROM DATA GROUP BY library, date ORDER BY total_requests DESC
        );''')
    conn.commit()

    # Create totals view
    c.execute('''CREATE VIEW IF NOT EXISTS totals AS
        SELECT
            *,
            total_requests / days AS requests_per_day,
            total_bandwidth / days AS bandwidth_per_day,
            total_bandwidth / total_requests AS bandwidth_per_request
        FROM
        (
            SELECT
                year,
                month,
                date,
                days,
                (CASE
                    WHEN bandwidth_3_days IS NULL THEN bandwidth_1_percent * 100
                    ELSE (bandwidth_1_percent * 100 * 0.75) + ((bandwidth_3_days / 3) * days * 0.25)
                END) AS total_bandwidth,
                (CASE
                    WHEN requests_3_days IS NULL THEN requests_1_percent * 100
                    ELSE (requests_1_percent * 100 * 0.75) + ((requests_3_days / 3) * days * 0.25)
                END) AS total_requests
            FROM
            (
                SELECT
                    bandwidth_1_percent,
                    bandwidth_3_days,
                    requests_1_percent,
                    requests_3_days,
                    year,
                    month,
                    (julianday(DATE(year || "-" || printf("%02d", month) || "-01", "+1 month")) - julianday(year || "-" || printf("%02d", month) || "-01")) AS days,
                    year || "-" || printf("%02d", month) as date
                FROM DATA_TOTALS ORDER BY date DESC
            )
        );''')
    conn.commit()
    conn.close()


def table_data(request_data: List[Dict[str, Union[int, float, str]]]) -> str:
    # Create the header
    header = beautifultable.BeautifulTable(max_width=1000, default_alignment=beautifultable.ALIGN_LEFT)
    header.set_style(beautifultable.STYLE_MARKDOWN)
    header.column_headers = ["#", "Requests", "Bandwidth", "cdnjs Resource URL"]
    header.append_row(["", "", "", ""])

    # Create the base table
    base_table = beautifultable.BeautifulTable(max_width=1000, default_alignment=beautifultable.ALIGN_LEFT)
    base_table.set_style(beautifultable.STYLE_MARKDOWN)
    base_table.detect_numerics = False  # This breaks the formatting

    # Sort the data
    request_data = sorted(request_data, key=lambda x: x["requests"], reverse=True)

    # Generate the table
    for i, row in enumerate(request_data):
        try:
            base_table.append_row([
                "{:,}".format(i + 1),
                "{:,}".format(row["requests"]),
                "{:,.2f}".format(row["bandwidth"]),
                "[{0}](https://{0})".format(row["resource"])
            ])
        except:
            continue

    # Export header + table
    base_table.column_alignments[2] = beautifultable.ALIGN_RIGHT
    header = str(header)
    base_table = str(base_table)
    return header[:header.rfind("\n")] + "\n" + base_table


def over_under_nearly(exact: Union[float, int], rounded: int) -> str:
    return "over" if exact > rounded else ("just under" if rounded - exact <= 0.2 else "nearly")


def get_template(template_file: str, variables: dict) -> str:
    # Load in template file
    with open("template/" + template_file) as f:
        template = f.read()

    # Substitute in variables
    for key, value in variables.items():
        template = template.replace("{{" + key + "}}", str(value))

    return template


def create_file(table_string: str, month: int, year: int, total_data: dict):
    variables = {
        "MONTH": calendar.month_name[month],
        "YEAR": year,
        "DAYS": calendar.monthrange(year, month)[1],
        "TABLE": table_string
    }

    # Requests
    REQUESTS_1_PER_TOTAL = total_data["REQUESTS_1_PER"] * 100
    REQUESTS_3_DAY_TOTAL = None if total_data["REQUESTS_3_DAY"] is None else (total_data["REQUESTS_3_DAY"] / 3) * variables["DAYS"]
    REQUESTS = REQUESTS_1_PER_TOTAL if REQUESTS_3_DAY_TOTAL is None else REQUESTS_1_PER_TOTAL * .75 + REQUESTS_3_DAY_TOTAL * .25
    variables.update({
        "REQUESTS_1_PER": "{:,}".format(total_data["REQUESTS_1_PER"]),
        "REQUESTS_1_PER_TOTAL": "{:,.0f}".format(REQUESTS_1_PER_TOTAL),
        "REQUESTS_3_DAY": "" if total_data["REQUESTS_3_DAY"] is None else "{:,}".format(total_data["REQUESTS_3_DAY"]),
        "REQUESTS_3_DAY_TOTAL": "" if REQUESTS_3_DAY_TOTAL is None else "{:,.0f}".format(REQUESTS_3_DAY_TOTAL),
        "REQUESTS": "{:,.0f}".format(REQUESTS),
        "REQUESTS_STAT": "",
        "REQUESTS_HIGHLIGHT": "",  # Key highlights
        "REQUESTS_DESCRIPTION": ""  # Total number of requests
    })

    # Requests insights
    requests_billion = REQUESTS / 1000000000
    requests_billion_rounded = round(requests_billion)
    variables["REQUESTS_STAT"] = over_under_nearly(requests_billion, requests_billion_rounded) \
                                 + " {:,.0f} billion requests".format(requests_billion_rounded)
    state = bool(round(random()))
    variables["REQUESTS_HIGHLIGHT"] = ("This month ({} {}), ".format(variables["MONTH"], year) if state else "") \
                                      + "cdnjs served **{}**".format(variables["REQUESTS_STAT"]) \
                                      + (" in {} {}.".format(variables["MONTH"], year) if not state else ".")
    variables["REQUESTS_DESCRIPTION"] = variables["REQUESTS_STAT"].capitalize() \
                                        + " or {} {:,.1f} billion requests {} day of {}".format(
        choice(["around", "roughly", "approximately"]),
        requests_billion / variables["DAYS"],
        choice(["every", "every single", "each"]), variables["MONTH"])

    # Sites
    SITES = total_data["SITES_1_PER"] * 100
    variables.update({
        "SITES_1_PER": "{:,}".format(total_data["SITES_1_PER"]),
        "SITES": "{:,.0f}".format(SITES),
        "SITES_STAT": "",
        "SITES_HIGHLIGHT": "",  # Key highlights
        "SITES_DESCRIPTION": ""  # Websites using cdnjs
    })

    # Sites insights
    variables["SITES_STAT"] = "{:,.2f} billion {} websites used cdnjs {}".format(
        SITES / 1000000000,
        choice(["unique", "different"]),
        choice(["assets", "resources"])
    )
    state = not state
    variables["SITES_HIGHLIGHT"] = ("In {}, ".format(variables["MONTH"]) if state else "") \
                                      + "**{}**".format(variables["SITES_STAT"]) \
                                      + (" this month!" if not state else "!")
    variables["SITES_DESCRIPTION"] = variables["SITES_STAT"].capitalize() \
                                        + " in {} {}".format(variables["MONTH"], year)

    # Bandwidth
    BANDWIDTH_1_PER_TOTAL_GB = total_data["BANDWIDTH_1_PER"] * 100
    BANDWIDTH_1_PER_TOTAL_PB = BANDWIDTH_1_PER_TOTAL_GB / 1000000
    BANDWIDTH_3_DAY_TOTAL_GB = None if total_data["BANDWIDTH_3_DAY"] is None else (total_data["BANDWIDTH_3_DAY"] / 3) * variables["DAYS"]
    BANDWIDTH_3_DAY_TOTAL_PB = None if BANDWIDTH_3_DAY_TOTAL_GB is None else BANDWIDTH_3_DAY_TOTAL_GB / 1000000
    BANDWIDTH_GB = BANDWIDTH_1_PER_TOTAL_GB if BANDWIDTH_3_DAY_TOTAL_GB is None else BANDWIDTH_1_PER_TOTAL_GB * .75 + BANDWIDTH_3_DAY_TOTAL_GB * .25
    BANDWIDTH_PB = BANDWIDTH_GB / 1000000
    variables.update({
        "BANDWIDTH_1_PER": "{:,}".format(total_data["BANDWIDTH_1_PER"]),
        "BANDWIDTH_1_PER_TOTAL_GB": "{:,.1f}".format(BANDWIDTH_1_PER_TOTAL_GB),
        "BANDWIDTH_1_PER_TOTAL_PB": "{:,.2f}".format(BANDWIDTH_1_PER_TOTAL_PB),
        "BANDWIDTH_3_DAY": "" if total_data["BANDWIDTH_3_DAY"] is None else "{:,}".format(total_data["BANDWIDTH_3_DAY"]),
        "BANDWIDTH_3_DAY_TOTAL_GB": "" if BANDWIDTH_3_DAY_TOTAL_GB is None else "{:,.1f}".format(BANDWIDTH_3_DAY_TOTAL_GB),
        "BANDWIDTH_3_DAY_TOTAL_PB": "" if BANDWIDTH_3_DAY_TOTAL_PB is None else "{:,.2f}".format(BANDWIDTH_3_DAY_TOTAL_PB),
        "BANDWIDTH_GB": "{:,.1f}".format(BANDWIDTH_GB),
        "BANDWIDTH_PB": "{:,.2f}".format(BANDWIDTH_PB),
        "BANDWIDTH_STAT": "",
        "BANDWIDTH_HIGHLIGHT": "",  # Key highlights
        "BANDWIDTH_DESCRIPTION": ""  # Total bandwidth usage
    })

    # Bandwidth insights
    variables["BANDWIDTH_STAT"] = "a {} consumption of {} PB of data".format(
        choice(["massive", "huge"]), variables["BANDWIDTH_PB"])
    state = not state
    variables["BANDWIDTH_HIGHLIGHT"] = ("This month, " if state else "") \
                                       + "cdnjs used **{}** to serve these requests" \
                                           .format(variables["BANDWIDTH_STAT"]) \
                                       + (" this month." if not state else ".")
    variables["BANDWIDTH_DESCRIPTION"] = "This gives cdnjs {} for requests {}".format(
        variables["BANDWIDTH_STAT"].replace("PB", "petabytes").replace("consumption", "bandwidth consumption"),
        choice(["this month", "in {}".format(variables["MONTH"])]))

    # Per day key highlight
    bandwidth_days_tb = (BANDWIDTH_GB / variables["DAYS"]) / 1000
    bandwidth_days_tb_rounded = round(bandwidth_days_tb)
    requests_days_billion = (REQUESTS / variables["DAYS"]) / 1000000000
    state = bool(round(random()))
    variables["PER_DAY_HIGHLIGHT"] = "{} **{} {:,} {} of data and {:,.1f} billion requests {} day** (averaged)." \
        .format(
        "That's" if state else "That works out to",
        over_under_nearly(bandwidth_days_tb, bandwidth_days_tb_rounded),
        bandwidth_days_tb_rounded,
        "terabytes" if state else "TB",
        requests_days_billion,
        choice(["each", "every"])
    )

    # Per request key highlight
    bandwidth_requests_kb = (BANDWIDTH_GB / REQUESTS) * 1000000
    state = bool(round(random()))
    variables["PER_REQUEST_HIGHLIGHT"] = "In {}, **each request to cdnjs{} used only {:,.2f} KB of data{}**." \
        .format(
        variables["MONTH"],
        " (on average)" if state else "",
        bandwidth_requests_kb,
        "" if state else " on average",
    )

    # Connect to DB
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Get top assets
    c.execute("SELECT library, version, file, requests, bandwidth FROM DATA WHERE month = ? AND year = ? ORDER BY requests DESC LIMIT 5", (month, year))
    rows = c.fetchall()
    for i, row in enumerate(rows):
        variables["TOP_ASSETS_" + str(i + 1) + "_LIBRARY"] = row[0]
        variables["TOP_ASSETS_" + str(i + 1) + "_VERSION"] = row[1]
        variables["TOP_ASSETS_" + str(i + 1) + "_FILE"] = row[2]
        variables["TOP_ASSETS_" + str(i + 1) + "_REQUESTS"] = "{:,.2f} billion".format((row[3] * 100) / 1000000000)
        variables["TOP_ASSETS_" + str(i + 1) + "_BANDWIDTH"] = "{:,.2f} TB".format((row[4] * 100) / 1000)

    # Get top libraries
    c.execute("SELECT library, total_requests, total_bandwidth FROM libraries WHERE month = ? AND year = ? ORDER BY total_requests DESC LIMIT 5", (month, year))
    rows = c.fetchall()
    for i, row in enumerate(rows):
        variables["TOP_LIBRARIES_" + str(i + 1) + "_NAME"] = row[0]
        variables["TOP_LIBRARIES_" + str(i + 1) + "_REQUESTS"] = "{:,.2f} billion".format(row[1] / 1000000000)
        variables["TOP_LIBRARIES_" + str(i + 1) + "_BANDWIDTH"] = "{:,.2f} TB".format(row[2] / 1000)

    # Done with DB
    conn.close()

    # Load in requests template
    variables["REQUESTS_PRETEXT"] = get_template("requests_1_per.md" if REQUESTS_3_DAY_TOTAL is None else "requests_combined.md", variables)

    # Load in bandwidth template
    variables["BANDWIDTH_PRETEXT"] = get_template("bandwidth_1_per.md" if REQUESTS_3_DAY_TOTAL is None else "bandwidth_combined.md", variables)

    # Final template
    template = get_template("template.md", variables)

    # Save to new file
    os.makedirs("./{}".format(year), exist_ok=True)
    with open("./{}/cdnjs_{}_{}.md".format(year, variables["MONTH"], year), "w+") as f:
        f.write(template)


if __name__ == "__main__":
    REQUESTS_1_PER = 1500000000
    REQUESTS_3_DAY = None
    SITES_1_PER = 0
    BANDWIDTH_1_PER = 30000.00  # GB
    BANDWIDTH_3_DAY = None  # GB
    RAW_TABLE_DATA_URL = ""  # 1% data
    RAW_TABLE_DATA_ORDER = ["requests", "resources", "bandwidth"]
    MONTH = 1
    YEAR = 2020

    stats = {
        "REQUESTS_1_PER": REQUESTS_1_PER,
        "REQUESTS_3_DAY": REQUESTS_3_DAY,
        "SITES_1_PER": SITES_1_PER,
        "BANDWIDTH_1_PER": BANDWIDTH_1_PER,
        "BANDWIDTH_3_DAY": BANDWIDTH_3_DAY
    }
    regex = generate_regex(RAW_TABLE_DATA_ORDER)
    items = parse_raw(RAW_TABLE_DATA_URL, regex)
    database_data(items, MONTH, YEAR, stats)
    request_table = table_data(items)
    create_file(request_table, MONTH, YEAR, stats)

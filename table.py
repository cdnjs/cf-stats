"""
A quick script to parse the top 100 requests stats
dumps that Cloudflare give us into a clean table.
"""
import requests
import re
import beautifultable
import sqlite3
from typing import List, Dict, Union

def generate_regex(order: List[str]) -> str:
    final = []
    patterns = {
        "requests": "(?P<requests>\d+)",
        "resources": "(?P<resource>\S+)",
        "bandwidth": "(?P<bandwidth>\d+(?:\.\d+)?)"
    }
    joiner = "[\s|│]*"
    for item in order:
        if item in patterns:
            final.append(patterns[item])
    final = "^" + joiner + joiner.join(final) + joiner + "$"
    return final

def parse_raw(url: str, regex: str) -> List[Dict[str, Union[int, float, str]]]:
    # Get the raw dump from the url
    raw = requests.get(url).text
    data = []
    file_regex = "^cdnjs\.cloudflare\.com\/ajax\/libs\/(?P<library>.+?)\/(?P<version>.+?)\/(?P<file>.+)$"

    # Iterate over each line of the dump
    for line in raw.split("\n"):
        try:
            # Attempt to find the components through regex
            x = re.search(regex, line)
            y = x.groupdict()

            # Ensure correct datatypes
            y["requests"] = int(y["requests"])
            y["bandwidth"] = float(y["bandwidth"])

            # Parse resource further
            z = re.search(file_regex, y["resource"]).groupdict()
            for key, value in z.items():
                y[key] = value

            data.append(y)
        except:
            continue
    return data

def table_data(data: List[Dict[str, Union[int, float, str]]]) -> str:
    # Create the header
    header = beautifultable.BeautifulTable(max_width=1000, default_alignment=beautifultable.ALIGN_LEFT)
    header.set_style(beautifultable.STYLE_MARKDOWN)
    header.column_headers = ["#", "Requests", "Bandwidth", "cdnjs Resource URL"]
    header.append_row(["", "", "", ""])

    # Create the base table
    table = beautifultable.BeautifulTable(max_width=1000, default_alignment=beautifultable.ALIGN_LEFT)
    table.set_style(beautifultable.STYLE_MARKDOWN)
    table.detect_numerics = False  # This breaks the formatting

    # Sort the data
    data = sorted(data, key=lambda x: x["requests"], reverse=True)

    # Generate the table
    for i, row in enumerate(data):
        try:
            table.append_row([
                "{:,}".format(i+1),
                "{:,}".format(row["requests"]),
                "{:,.2f}".format(row["bandwidth"]),
                "[{0}](https://{0})".format(row["resource"])
            ])
        except:
            continue

    # Export header + table
    table.column_alignments[2] = beautifultable.ALIGN_RIGHT
    header = str(header)
    table = str(table)
    return header[:header.rfind("\n")] + "\n" + table

def database_data(data: List[Dict[str, Union[int, float, str]]]):
    # Create db (drop old data/table, create new table)
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS DATA''')
    c.execute('''CREATE TABLE DATA (resource text, bandwidth float, requests integer, library text, version text, file text)''')
    conn.commit()

    # Export all the data
    for row in data:
        c.execute('''INSERT INTO DATA (resource,bandwidth,requests,library,version,file) VALUES (?,?,?,?,?,?)''', [
            row["resource"], row["bandwidth"], row["requests"], row["library"], row["version"], row["file"]
        ])
    conn.commit()
    conn.close()

regex = generate_regex(["requests", "resources", "bandwidth"])
data = parse_raw("", regex)
database_data(data)
print(table_data(data))

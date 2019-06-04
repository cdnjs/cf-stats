"""
A quick script to parse the top 100 requests stats
dumps that Cloudflare give us into a clean table.
"""
import requests
import re
import beautifultable
from typing import List, Dict, Union

def generate_regex(order: List[str]) -> str:
    final = []
    patterns = {
        "requests": "(?P<requests>\d+)",
        "resources": "(?P<resource>\S+)",
        "bandwidth": "(?P<bandwidth>\d+(?:\.\d+)?)"
    }
    for item in order:
        if item in patterns:
            final.append(patterns[item])
    final = "^\s*" + "\s*".join(final) + "\s*$"
    return final

def parse_raw(url: str, regex: str) -> List[Dict[str, Union[int, float, str]]]:
    # Get the raw dump from the url
    raw = requests.get(url).text
    data = []

    # Iterate over each line of the dump
    for line in raw.split("\n"):
        try:
            # Attempt to find the components through regex
            x = re.search(regex, line)
            y = x.groupdict()

            # Ensure correct datatypes
            y["requests"] = int(y["requests"])
            y["bandwidth"] = float(y["bandwidth"])
            data.append(y)
        except:
            continue
    return data

def format_data(data: List[Dict[str, Union[int, float, str]]]) -> str:
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

def table_from_raw(url: str, order: List[str]) -> str:
    regex = generate_regex(order)
    data = parse_raw(url, regex)
    table = format_data(data)
    return table

print(table_from_raw("", ["requests", "resources", "bandwidth"]))
        
    

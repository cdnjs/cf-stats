"""
A script that takes the stats Cloudflare provides from our local DB and generates the repo READMEs.
Also handles committing the all the monthly stats changes to Git.
"""

import calendar
import sqlite3
import subprocess

import utils


def readme():
    # Connect to the DB and get all the unique months/years we have data for
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT DISTINCT year, month FROM totals ORDER BY year DESC, month DESC")
    rows = c.fetchall()

    # Group by year
    by_year = {}
    for item in rows:
        if item["year"] not in by_year:
            by_year[item["year"]] = []
        by_year[item["year"]].append(item["month"])

    # Manually inject months with missing data
    by_year[2021] += [10]
    by_year[2019] += [2]

    # Generate the stats lists for each year
    stats_by_year = {}
    years = sorted(by_year.keys(), reverse=True)
    for year in years:
        stats_list = ["* [{0} {1}]({1}/cdnjs_{0}_{1}.md)".format(calendar.month_name[month], year) for month in sorted(by_year[year], reverse=True)]
        stats_by_year[year] = "\n".join(stats_list)

    # Generate the root README
    with open("./README.md", "w+") as f:
        f.write(utils.get_template(
            "root_readme.md",
            {
                "LATEST_STATS": "**📈 [{0} {1}]({1}/cdnjs_{0}_{1}.md)**".format(calendar.month_name[rows[0]["month"]], rows[0]["year"]),
                "PREVIOUS_STATS": "\n".join(["### [{0}]({0})\n\n{1}\n".format(year, stats_by_year[year]) for year in years]).strip()
            }
        ))

    # Generate the year READMEs
    for year in years:
        with open(f"./{year}/README.md", "w+") as f:
            f.write(utils.get_template(
                "year_readme.md",
                {
                    "YEAR": year,
                    "STATS": stats_by_year[year].replace("{}/".format(year), "")
                }
            ))


def commit(month, year):
    month_name = calendar.month_name[month]
    month_year = f"{month_name} {year}"

    # Switch to a new branch for the month
    subprocess.run(["git", "switch", "-C", month_name.lower()])

    # Stage + commit all the Markdown files
    subprocess.run(["git", "add", "README.md", f"{year}/README.md", f"{year}/cdnjs_{month_name}_{year}.md"])
    subprocess.run(["git", "commit", "-m", f"Stats: {month_year}"])

    # Stage + commit the DB file
    subprocess.run(["git", "add", "data.db"])
    subprocess.run(["git", "commit", "-m", f"Data: {month_year}"])

    # Stage + commit the graphs
    subprocess.run(["git", "add", "*.png"])
    subprocess.run(["git", "commit", "-m", f"Graphs: {month_year}"])

    # Create pull request on GitHub
    subprocess.run(["git", "push", "-u", "origin", month_name.lower()])
    subprocess.run(["gh", "pr", "create", "--title", month_year, "--body", f"🗄 {month_year} database data.\n📈 {month_year} top resources & totals graphs.\n🎉 {month_year} stats from Cloudflare."])

    # Switch back to master
    subprocess.run(["git", "switch", "master"])


if __name__ == "__main__":
    readme()

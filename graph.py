"""
A script that takes the stats Cloudflare provides from our local DB and generates fun graphs.
"""

import sqlite3

import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Connect to the DB and get all the data ever
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM DATA")
    rows = c.fetchall()


    # DB item to year-month
    def ym(item):
        return "{}-{:02}".format(item["year"], item["month"])


    # DB item to lib/ver/file
    def fn(item):
        return "{}/{}/{}".format(item["library"], item["version"], item["file"])


    # Compile the data by each month (year-month)
    by_month = {}
    for item in rows:
        this_ym = ym(item)
        if this_ym not in by_month:
            by_month[this_ym] = []
        by_month[this_ym].append(item)

    # Sort the data each month and get the top x
    limit = 5
    for month in by_month:
        by_month[month].sort(key=lambda x: x["requests"], reverse=True)
        by_month[month] = [{
            "position": i + 1,
            "month": month,
            "requests": f["requests"],
            "bandwidth": f["bandwidth"],
            "library": f["library"],
            "version": f["version"],
            "file": f["file"]
        } for i, f in enumerate(by_month[month][:limit])]
        new = {}
        for item in by_month[month]:
            new[fn(item)] = item
        by_month[month] = new

    # Find every file in the top x across the months
    all_files = set()
    for month in by_month:
        for file in by_month[month]:
            all_files.add(file)

    # Generate by file with every month (None if not in that month)
    by_file = {}
    for file in all_files:
        by_file[file] = {}
        for month in by_month:
            if file in by_month[month]:
                by_file[file][month] = by_month[month][file]
            else:
                by_file[file][month] = None

    # Convert the by file data to plottable data
    plot = {}
    for file in by_file:
        plot[file] = [[], []]
        months = sorted(list(by_file[file].items()), key=lambda x: x[0])
        for month, data in months:
            plot[file][0].append(month)
            if data:
                plot[file][1].append(data["position"])
            else:
                plot[file][1].append(None)

    # Do the plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    ax.set(ylim=(limit + 0.5, 0.5))
    ax.set_yticks(range(1, limit + 1)[::-1])
    for file in plot:
        ax.plot(*plot[file], label=file, marker="o", markersize=4)
    ax.set_title("cdnjs Top 5 Resources")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=1)
    plt.show()
    fig.savefig("cdnjs_top_5_resources.png")

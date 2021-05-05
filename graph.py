"""
A script that takes the stats Cloudflare provides from our local DB and generates fun graphs.
"""

import sqlite3
from datetime import datetime

import matplotlib.pyplot as plt


# DB item to year-month
def ym(item):
    return "{}-{:02}".format(item["year"], item["month"])


# DB item to lib/ver/file
def fn(item):
    return "{}/{}/{}".format(item["library"], item["version"], item["file"])


def top_5_graph(data_by_month, limit, title, filename):
    # Find every item in the top x across the months
    all_items = set()
    for month in data_by_month:
        for item in data_by_month[month]:
            all_items.add(item)

    # Generate by item with every month (None if not in that month)
    by_item = {}
    for item in all_items:
        by_item[item] = {}
        for month in data_by_month:
            if item in data_by_month[month]:
                by_item[item][month] = data_by_month[month][item]
            else:
                by_item[item][month] = None

    # Convert the by item data to plottable data
    plot = {}
    for item in by_item:
        plot[item] = [[], []]
        months = sorted(list(by_item[item].items()), key=lambda x: x[0])
        for month, data in months:
            plot[item][0].append(month)
            if data:
                plot[item][1].append(data["position"])
            else:
                plot[item][1].append(None)

    # Set the correct order (1 -> 5, newest -> oldest)
    order = []
    for month in sorted(list(data_by_month.keys()), reverse=True):
        for item in data_by_month[month]:
            if item not in order:
                order.append(item)

    # Do the plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    ax.set(ylim=(limit + 0.5, 0.5))
    ax.set_yticks(range(1, limit + 1)[::-1])
    for item in order:
        ax.plot(*plot[item],
                label=(item if item in order[:8] else None),
                marker="o",
                markersize=4,
                color=(None if item in order[:8] else (0.2, 0.2, 0.2, 1)))
    ax.set_title(title)
    ax.tick_params(axis="x", labelsize=8, labelrotation=45)
    fig.subplots_adjust(bottom=0.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=1)
    plt.show()
    fig.savefig(filename)


def top_5_resources():
    # Connect to the DB and get all the data ever
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM DATA")
    rows = c.fetchall()

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

    # Plot and save
    top_5_graph(by_month, limit, "cdnjs Top 5 Resources", "cdnjs_top_5_resources.png")


def top_5_libraries():
    # Connect to the DB and get all the data ever
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM libraries")
    rows = c.fetchall()

    # Compile the data by each month (year-month)
    by_month = {}
    for item in rows:
        if item["date"] not in by_month:
            by_month[item["date"]] = []
        by_month[item["date"]].append(item)

    # Sort the data each month and get the top x
    limit = 5
    for month in by_month:
        by_month[month].sort(key=lambda x: x["total_requests"], reverse=True)
        by_month[month] = [{
            "position": i + 1,
            "month": month,
            "requests": f["total_requests"],
            "bandwidth": f["total_bandwidth"],
            "library": f["library"],
        } for i, f in enumerate(by_month[month][:limit])]
        new = {}
        for item in by_month[month]:
            new[item["library"]] = item
        by_month[month] = new

    # Plot and save
    top_5_graph(by_month, limit, "cdnjs Top 5 Libraries", "cdnjs_top_5_libraries.png")


def requests_and_bandwidth_graph(requests_data, bandwidth_data, requests_title, bandwidth_title, title, filename):
    plt.style.use("dark_background")
    fig, ax1 = plt.subplots()

    use_precise_bil = max(requests_data[1]) - min(requests_data[1]) < 4000000000

    ax1.plot(*requests_data, label=requests_title, color="#D9643A")
    ax1.tick_params(axis="y", labelcolor="#D9643A")
    if use_precise_bil:
        ax1.set_yticklabels(["{:,.1f} bil.".format(x / 1000000000) for x in ax1.get_yticks().tolist()])
    else:
        ax1.set_yticklabels(["{:,.0f} bil.".format(x / 1000000000) for x in ax1.get_yticks().tolist()])
    ax1.legend(loc="upper left", bbox_to_anchor=(0, -0.175), ncol=1, borderpad=0.75, handletextpad=1.5)

    use_pb = (sum(bandwidth_data[1]) / len(bandwidth_data[1])) > 1000000

    ax2 = ax1.twinx()
    ax2.plot(*bandwidth_data, label=bandwidth_title, color="#1EADAE")
    ax2.tick_params(axis="y", labelcolor="#1EADAE")
    if use_pb:
        ax2.set_yticklabels(["{:,.1f} PB".format(x / 1000000) for x in ax2.get_yticks().tolist()])
    else:
        ax2.set_yticklabels(["{:,.0f} TB".format(x / 1000) for x in ax2.get_yticks().tolist()])
    ax2.legend(loc="upper right", bbox_to_anchor=(1, -0.175), ncol=1, borderpad=0.75, handletextpad=1.5)

    ax1.set_title(title)
    ax1.tick_params(axis="x", labelsize=8, labelrotation=45)
    plt.show()
    fig.savefig(filename)


def total_requests_and_bandwidth():
    # Connect to the DB and get all the total data ever (from the view, not the raw table)
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM totals")
    rows = c.fetchall()

    # Generate the plottable data
    requests = [[], []]
    bandwidth = [[], []]
    months = sorted(rows, key=lambda x: x['date'])
    for month in months:
        the_date = datetime.strptime(month['date'] + "-01", "%Y-%m-%d").date()
        requests[0].append(the_date)
        requests[1].append(month['total_requests'])
        bandwidth[0].append(the_date)
        bandwidth[1].append(month['total_bandwidth'])

    # Do the plot
    requests_and_bandwidth_graph(requests, bandwidth, "Total Requests", "Total Bandwidth",
                                 "cdnjs Total Requests and Bandwidth", "cdnjs_total_requests_and_bandwidth.png")


def daily_requests_and_bandwidth():
    # Connect to the DB and get all the total data ever (from the view, not the raw table)
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM totals")
    rows = c.fetchall()

    # Generate the plottable data
    requests = [[], []]
    bandwidth = [[], []]
    months = sorted(rows, key=lambda x: x['date'])
    for month in months:
        the_date = datetime.strptime(month['date'] + "-01", "%Y-%m-%d").date()
        requests[0].append(the_date)
        requests[1].append(month['requests_per_day'])
        bandwidth[0].append(the_date)
        bandwidth[1].append(month['bandwidth_per_day'])

    # Do the plot
    requests_and_bandwidth_graph(requests, bandwidth, "Avg. Daily Requests", "Avg. Daily Bandwidth",
                                 "cdnjs Avg. Daily Requests and Bandwidth", "cdnjs_daily_requests_and_bandwidth.png")


if __name__ == "__main__":
    top_5_resources()
    top_5_libraries()
    total_requests_and_bandwidth()
    daily_requests_and_bandwidth()

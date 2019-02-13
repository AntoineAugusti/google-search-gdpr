#!/usr/bin/env python
import json
from argparse import ArgumentParser
from collections import defaultdict

import pandas as pd

parser = ArgumentParser()
parser.add_argument("filepath", help="The full path to the Google Search JSON file")
args = parser.parse_args()

with open(args.filepath) as f:
    data = json.load(f)

res = defaultdict(list)
for record in data:
    if record["title"].startswith("Searched for "):
        res["search"].append(record["title"].replace("Searched for ", ""))
        res["time"].append(record["time"])

        if "locations" in record:
            map_url = record["locations"][0]
            latitude, longitude = map(float, map_url["url"].split("=")[1].split(","))
        else:
            latitude, longitude = None, None
        res["latitude"].append(latitude)
        res["longitude"].append(longitude)


df = pd.DataFrame(res, columns=res.keys())
df["time"] = pd.to_datetime(df["time"])

df["year"] = df.time.dt.strftime("%Y")
df["year_month"] = df.time.dt.strftime("%Y-%m")
df["month"] = df.time.dt.strftime("%m")
df["year_week"] = df.time.dt.strftime("%G-%V")
df["day"] = df.time.dt.strftime("%Y-%m-%d")
df["weekday"] = df.time.dt.strftime("%w")
df["hour"] = df.time.dt.strftime("%H")

df.to_csv("data.csv", index=False)

"""
Functions useful for converting data from CSV to JSON and vice-versa:
* csv_to_json
* json_to_csv

REFERENCES:
https://en.wikipedia.org/wiki/Comma-separated_values
https://en.wikipedia.org/wiki/JSON
"""

import csv
import json
from pathlib import Path

import pandas as pd


def csv_to_json(filename: str) -> str:
    """
    Convert data from CSV to JSON

    >>> csv_to_json()

    >>> csv_to_json()

    """
    file = open(filename, "r")
    dict_reader = csv.DictReader(file)

    dict_from_csv = list(dict_reader)[0]
    json_from_csv = json.dumps(dict_from_csv)
    file.close()

    return json_from_csv


def json_to_csv(filename: str) -> str:
    """
    Convert data from JSON to CSV

    >>> json_to_csv()

    >>> json_to_csv()

    """
    jsonpath = Path(filename)

    with jsonpath.open("r", encoding="utf-8") as datafile:
        data = json.loads(datafile.read())

    df = pd.json_normalize(data)
    return df

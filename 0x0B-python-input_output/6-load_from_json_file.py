#!/usr/bin/python3
"""mthod to load from json"""
import json


def load_from_json_file(filename):
    """load a json file”"""
    with open(filename, mode="r", encoding="utf-8") as newfile:
        return json.loads(newfile.read())
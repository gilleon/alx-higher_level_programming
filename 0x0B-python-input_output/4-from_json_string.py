#!/usr/bin/python3
"""method to parase json to object"""
import json


def from_json_string(my_str):
    """retun ogject from json"""
    return json.loads(my_str)
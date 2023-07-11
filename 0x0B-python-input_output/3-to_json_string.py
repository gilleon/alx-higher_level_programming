#!/usr/bin/python3
"""method to parse json"""
import json


def to_json_string(my_obj):
    """Method to return parse object as json"""
    return json.dumps(my_obj)
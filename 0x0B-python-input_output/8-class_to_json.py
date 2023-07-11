#!/usr/bin/python3
"""Class to JSON method"""


def class_to_json(obj):
    """returns the dictionary description with
    simple data structure
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
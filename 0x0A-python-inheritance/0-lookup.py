#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """lookup function
    Returns: a list of available attributes
    and methods of an object"""
    return dir(obj)

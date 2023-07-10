#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(obj, name, value):
    """Method checking if attribute can be set and sets
    where possible"""
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

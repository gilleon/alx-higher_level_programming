#!/usr/bin/python3
"""method for readding file"""


def read_file(filename=""):
    """method to opeing a file"""
    with open(filename, "r", encoding="utf-8") as newfile:
        print(newfile.read(), end="")

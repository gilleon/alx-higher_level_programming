#!/usr/bin/python3
"""Method to add text to an exiting file"""


def append_write(filename="", text=""):
    """Mtd that appends a string to a text file and returns no.\
        of chars added"""
    with open(filename, mode="a", encoding="utf-8") as newfile:
        return newfile.write(text)
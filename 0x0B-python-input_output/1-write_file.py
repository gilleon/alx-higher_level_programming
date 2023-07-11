#!/usr/bin/python3
"""method to write to file"""


def write_file(filename="", text=""):
    """open and wirte to file"""
    with open(filename, mode="w", encoding="utf-8") as newfile:
        return newfile.write(text)
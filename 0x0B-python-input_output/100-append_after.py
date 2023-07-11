#!/usr/bin/python3
'''Module for append_after method.'''


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    newline = []
    with open(filename, mode="r", encoding="utf-8") as newfile:
        newline = newfile.readlines()
        i = 0
        while i < len(newline):
            if search_string in newline[i]:
                newline[i:i + 1] = [newline[i], new_string]
                i += 1
            i += 1
    with open(filename, mode="w", encoding="utf-8") as newfile:
        newfile.writelines(newline)

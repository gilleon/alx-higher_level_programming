#!/usr/bin/python3
def remove_char_at(str, n):
    stringc = ""
    for i in range(0, len(str)):
        if i != n:
            stringc += str[i]
    return stringc

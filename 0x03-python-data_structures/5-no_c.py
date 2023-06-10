#!/usr/bin/python3
def no_c(my_string):
    container = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            container += x
    str = container
    return str

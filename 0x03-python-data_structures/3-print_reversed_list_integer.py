#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    len = 0
    for x in my_list:
        len += 1
    for y in range(-1, -(len + 1), -1):
        print("{:d}".format(my_list[y]))

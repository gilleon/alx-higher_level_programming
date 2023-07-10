#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList class, Inherited from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

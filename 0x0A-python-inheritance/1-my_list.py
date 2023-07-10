#!/usr/bin/python3


class MyList(list):
    """MyList class, Inherited from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

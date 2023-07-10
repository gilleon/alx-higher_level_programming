#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """MyInt class decl"""
    def __eq__(self, other):
        """Overides operator =="""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides operator =!"""
        return int(self) == int(other)

#!/usr/bin/python3
"""Square class that access and update the private
attribute"""


class Square:
    """defines class with private attribute size"""
    def __init__(self, size=0):
        """Constructor.
        Arg:
            size: Length of square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter - sets the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public method that returns area"""
        return self.__size ** 2

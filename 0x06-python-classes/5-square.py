#!/usr/bin/python3
"""Square class built bases on 4"""


class Square:
    """defines a square with private instance attribute size"""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: Length of sqaure
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of size

        Raises:
            TypeError: If size is not an int
            ValueError; If size is less than 0
        """
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

    def my_print(self):
        """prints the square to stdout with char #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

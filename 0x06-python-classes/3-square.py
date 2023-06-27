#!/usr/bin/python3
"""Square class with method that checks area metric"""


class Square:
    """defines class with private instance attribute size"""
    def __init__(self, size=0):
        """Retrieves the value of size

        Raises:
            TypeError: If size is not an int
            ValueError; If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """public instance method returns the area"""
        return self.__size ** 2

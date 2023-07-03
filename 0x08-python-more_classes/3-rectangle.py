#!/usr/bin/python3
"""Rectanle module."""


class Rectangle:
    """class rectangle declaration"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle parameters"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width < 0:
                raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height < 0:
                raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        object width definition
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set variable
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        check for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        return area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string rep of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += "#" * self.__width
            output += "\n"

        return output.rstrip()

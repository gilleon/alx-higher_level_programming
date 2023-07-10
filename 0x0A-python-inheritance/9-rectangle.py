#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Init function"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle function"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

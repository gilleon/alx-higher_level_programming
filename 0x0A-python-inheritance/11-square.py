#!/usr/bin/python3
"""Square class inherited from rect class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class decl"""
    def __init__(self, size):
        """init square function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of a square fuunction"""
        return self.__size ** 2

    def __str__(self):
        """returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)

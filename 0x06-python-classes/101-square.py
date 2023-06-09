#!/usr/bin/python3
"""Square class"""


class Square:
    """defines class with private attribute size"""

    def __str__(self):
        """stringifyies a value"""
        return self.my_srep()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of the side of a square
            position: position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter - sets the value of size"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instance method returns current sqr area"""

        return self.__size ** 2

    def my_srep(self):
        """Returns string representation of this square."""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
            ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """Prints the square"""
        print(self.my_srep(), end="")

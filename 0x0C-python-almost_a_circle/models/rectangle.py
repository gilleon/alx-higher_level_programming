#!/usr/bin/python3
from models.base import Base
"""Base class for all models"""


class Rectangle(Base):
    """rectangle class

    Args:
        Base (_type_): _description_

    Raises:
        TypeError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """contructor for Rectangle

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """validates rectangle's attributes

        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def x(self):
        '''returns the x coordinate of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        '''returns the y coordinate of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    @property
    def width(self):
        '''return width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        '''return height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    def area(self):
        """method to calculate area of rectangle

        Returns:
            _type_: type of rectangle
        """
        return self.width * self.height

    def display(self):
        '''method to display rectangle'''
        rec_s = "\n" * self.y + (" " * self.x + "#" * self.width +
                                 "\n") * self.height
        print(rec_s, end="")

    def __str__(self):
        '''return string representation fo the args'''
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def __updArgsKwarg(self, id=None, width=None, height=None, x=None, y=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
            width (_type_, optional): _description_. Defaults to None.
            height (_type_, optional): _description_. Defaults to None.
            x (_type_, optional): _description_. Defaults to None.
            y (_type_, optional): _description_. Defaults to None.
        """
        args = locals()
        for k in args.keys():
            if args[k] is not None and k != "self" and k == "id":
                self.__dict__[k] = args[k]
            elif args[k] is not None and k != "self":
                self.__dict__["_" + type(self).__name__ + "__" + k] = args[k]

    def update(self, *args, **kwargs):
        """updates rectangle's attributes

        Args:
            *args (_type_): _description_
            **kwargs (_type_): _description_
        """
        if args:
            self.__updArgsKwarg(*args)
        elif kwargs:
            self.__updArgsKwarg(**kwargs)

    def to_dictionary(self):
        '''returns as dictionary'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

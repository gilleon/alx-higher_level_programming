#!/usr/bin/python3
'''implementation for square models base on rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (_type_, optional): _description_. Defaults to 0.
            y (_type_, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        '''returns string representation of square'''
        return "[{}] ({}) {}/{} - {}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.height)

    @property
    def size(self):
        '''returns size of square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """private method for updating square"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update square'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''returns dictionary representation of square'''
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}

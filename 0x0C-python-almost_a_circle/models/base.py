#!/usr/bin/python3
"""Base class module"""
import json
import csv
import turtle as t
import time
from random import randrange

class Base():
    """class Base

    Returns:
        _type_: _description_
    """    
    ___nb_objects = 0

    def __init__(self, id=None):
        """initialize the class

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.___nb_objects += 1
            self.id = Base.___nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to convert a list of dictionaries

        Args:
            list_dictionaries (_type_): _description_

        Returns:
            json_string: json string representation of
            list_dictionaries
        """        
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' method to save a list of dictionaries'''        
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """method to convert a json string to a list of dictionaries

        Args:
            json_string (_type_): _description_

        Returns:
            list_dictionaries: list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method to create an instance of the class

        Args:
            dictionary (_type_): _description_

        Returns:
            new: instance of the class
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """method to load a dictionary from a file

        Returns:
            _type_: _description_
        """        
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' method to save a list of dictionaries'''
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        ''' method to load a dictionary from a file'''
        ret = []
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for obj in reader:
                    v = [eval(i) for i in obj]
                    if cls.__name__ == "Rectangle":
                        dct = {"id": v[0], "width": v[1], "height": v[2],
                               "x": v[3], "y": v[4]}
                    elif cls.__name__ == "Square":
                        dct = {"id": v[0], "size": v[1], "x": v[2], "y": v[3]}
                    ret.append(cls.create(**dct))
            return ret
        except FileNotFoundError:
            return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """_summary_

        Args:
            list_rectangles (_type_): _description_
            list_squares (_type_): _description_
        """        
        t.bgcolor("green")
        t.color("red")
        t.clear()
        t.up()
        w_h = t.window_height()
        w_w = t.window_width()
        center = -(w_w/2 - 20), (w_h/2 - 20)
        l = w_w * 0.7
        s = 20
        t.setpos(center)        #+ve x
        t.down()
        t.forward(l)
        t.left(90)
        t.setpos(center)        #-ve y
        t.forward(s)
        t.left(90)
        t.setpos(center)        #-ve x
        t.forward(s)
        t.left(90)
        t.setpos(center)        #+ve y
        t.forward(l)
        t.left(90)
        t.up()
        t.setpos(center)

        
        t.colormode(255)
        for i in list_rectangles + list_squares:
            try:
                h = i.size
                w = i.size
            except AttributeError:
                h = i.height 
                w = i.width
            x = i.x
            y = i.y
            t.color("orange")
            t.fillcolor(randrange(256), randrange(256), randrange(256))
            t.begin_fill()
            t.up()
            t.setpos(center[0] + x, center[1] - y)
            t.down()
            t.pensize(1)
            t.seth(0)
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
            t.end_fill()
        time.sleep(20)
        t.bye()
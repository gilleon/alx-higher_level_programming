#!/usr/bin/python3
"""Student class with attributes"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """public initialization Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets dict"""
        return self.__dict__.copy()

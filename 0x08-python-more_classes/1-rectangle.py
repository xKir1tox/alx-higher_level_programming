#!/usr/bin/python3
""" class for defines a rectangle"""
class Rectangle:
    """ def width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """Private instance attribute: width"""
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width=value
    """Private instance attribute: height"""
    @property
    def height(self):
        return sef.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height=value

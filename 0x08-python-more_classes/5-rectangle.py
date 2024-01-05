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
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height=value
    def area(self):
        return (self.__width*self.__height)
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2*(self.__width+self.__height)
    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        """Return the printable representation of the Rectangle.
               Represents the rectangle with the # character.
        """
        rect = "Rectangle(" + str(self.__width)
        rect = rect + ", " + str(self.__height) + ")"
        return rect
    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

#!/usr/bin/python3
"""   class Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):



    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs class"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """Private instance attribute: width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    """Private instance attribute: height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    """Private instance attribute: x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    """Private instance attribute: y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__y != 0:
            for newline in range(self.__y):
                print()

        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))


    def __str__(self):
        """Returns formatted information display
               """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                             self.id, self.__x, self.__y, self.__width,
                                                             self.__height)

    def update(self, *args,**kwargs):
        '''
        assigns an argument to each attribute:
        '''
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """Returns dict representation
        """

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
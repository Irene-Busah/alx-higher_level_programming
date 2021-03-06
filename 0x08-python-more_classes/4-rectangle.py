#!/usr/bin/python3

"""Defining class Rectangle with two private instance attributes"""


class Rectangle:
    """Instantiating instance attributes
    Private instance attribute: width & height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.width == 0 or self.__height == 0:
            return ""
        shape = ""
        for height in range(self.__height):
            for width in range(self.__width):
                shape += "#"
            if height is not self.__height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        height = str(self.__height)
        width = str(self.__width)
        return 'Rectangle({}, {})'.format(width, height)

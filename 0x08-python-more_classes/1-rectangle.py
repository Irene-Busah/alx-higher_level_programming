#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Defining Rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiation of width and height with edge cases
        Attributes:
            width: private instance attribute
            height: private instance attribute
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height    
    @property
    def height(self):
        """Getter for height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """Setter for height with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        """Getter for width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """Setter for width with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

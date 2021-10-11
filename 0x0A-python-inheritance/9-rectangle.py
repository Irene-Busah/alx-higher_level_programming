#!/usr/bin/python3

"""Defining a class Rectangle that inherits from the BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiating the instance methods of the class Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        print('[Rectangle] ' + str(self.__width) + '/' + str(self.__height))

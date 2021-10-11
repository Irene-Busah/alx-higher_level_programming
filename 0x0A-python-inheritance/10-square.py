#!/usr/bin/python3

"""Defining the class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Instantiating the instance methods for the Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

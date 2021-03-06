#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Defining Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

    def area(self):
        """Return area of rectangle
        """
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare the area of both rectangles
        and return the largest of the two
        Arguments:
        rect_1: Rectangle 1
        rect_2: Rectangle 2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square"""
        return Rectangle(size, size)

    def perimeter(self):
        """Return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        height = str(self.__height)
        width = str(self.__width)
        return 'Rectangle({}, {})'.format(width, height)

    def __str__(self):
        if self.width == 0 or self.__height == 0:
            return ""
        shape = ""
        for height in range(self.__height):
            for width in range(self.__width):
                shape += str(self.print_symbol)
            if height is not self.__height - 1:
                shape += "\n"
        return shape

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

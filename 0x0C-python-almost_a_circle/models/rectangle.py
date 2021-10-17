#!/usr/bin/python3

"""Defining the class Rectangle which inherit from the Base class"""

from base import Base


class Rectangle(Base):
    """Instantiating the instance methods of the class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter"""
        return self.__x

    @y.setter
    def y(self, y):
        """Setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """pound pointer"""
        symbol = '#'
        shape = ""
        print("{}".format('\n' * self.__y), end=shape)
        for i in range(self.__height):
            print('{}{}'.format(' ' * self.__x, symbol * self.__y))

    def __str__(self):
        id = str(self.id)
        width = str(self.width)
        height = str(self.height)
        x = str(self.x)
        y = str(self.y)
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        arg = len(args)
        if arg >= 1:
            self.id = args[0]
        elif "id" in kwargs:
            self.id = kwargs["id"]
        if arg >= 2:
            self.width = args[1]
        elif "width" in kwargs:
            self.width = kwargs["width"]
        if arg >= 3:
            self.height = args[2]
        elif "height" in kwargs:
            self.height = kwargs["height"]
        if arg >= 4:
            self.x = args[3]
        elif "x" in kwargs:
            self.x = kwargs["x"]
        if arg >= 5:
            self.y = args[4]
        elif "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """ Dictionary """
        rec_dict = {}
        rec_dict['id'] = self.id
        rec_dict['width'] = self.__width
        rec_dict['height'] = self.__height
        rec_dict['x'] = self.__x
        rec_dict['y'] = self.__y
        return rec_dict

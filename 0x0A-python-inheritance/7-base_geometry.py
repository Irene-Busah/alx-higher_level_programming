#!/usr/bin/python3
""" Empty class Geometry """


class BaseGeometry:
    """ Class """

    def area(self):
            """ Area Exception """
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
            """ Integer validation """
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value < 0:
                raise ValueError("{} must be greater than zero".format(name))
            if value == 0:
                raise ValueError("{} must be greater than zero".format(name))

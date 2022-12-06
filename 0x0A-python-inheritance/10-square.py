#!/usr/bin/python3
"""
Contains parent class BaseGeometry
with public instance method area and integer_validation
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__
Contains subclass Square
with instantiation of private attribute size, validated by superclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implements a square from a rectangle"""
    def __init__(self, size):
        """initialize size of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
"""
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""


class Rectangle(BaseGeometry):
    """
    validates width and height values
    using integer_validator property inherited @ 7-base_geometry
    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height 

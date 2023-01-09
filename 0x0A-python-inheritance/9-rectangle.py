#!/usr/bin/python3
"""Class ``Rectangle`` inherits the ``BaseGeometry`` class."""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Class Definition"""

    def __init__(self, width, height):
        """Initialize the attributes"""
        super().integer_validation("width", width)
        super().integer_validation("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height

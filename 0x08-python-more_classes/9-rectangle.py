#!/usr/bin/python3
"""Module containing definintion of the ``Rectangle`` class."""


class Rectangle:
    """class definition of the ``Rectangle``"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): first parameter. the width of the rectangle
            height (int): second parameter. the height of the rectangle.

        Raises:
            TypeError: if any of the parameters is not an integer
            ValueError: if any of the parameters is less than 0
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("Width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """``width`` property

        Args:
            value (int): sets the value of the width variable.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """``height`` property

        Args:
            value (int): sets the value of the height variable.

        Raises:
            TypeError: If ``value`` is not an integer
            ValueError: If ``value`` is less than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of the rectangle"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)

                if i < self.__height - 1:
                    rect += '\n'
            return rect

    def __repr__(self):
        """Official string representtaion of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """When deleting an instance"""
        Rectangle.number_of_instances -= 1  # decrease the instance by one
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rect with the biggest area.
        Args:
            rect_1 (Rectangle): first instance
            rect_2 (Rectangle): second instance

        Raises:
            TypeError: if any of the parameters is not an instance of
                ``Rectangle``
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

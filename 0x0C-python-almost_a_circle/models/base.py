#!/usr/bin/python3
"""Module to contain the ``Base`` class"""


class Base:
    """Class definition of ``Base``"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the constructor of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

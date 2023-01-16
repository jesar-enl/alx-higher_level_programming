#!/usr/bin/python3
"""Module containing Square class inheriting
from the rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the size of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update the argument placement"""
        if args is not None and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                id, size = args
                self.id = id
                self.size = size
            elif len(args) == 3:
                id, size, x = args
                self.id = id
                self.size = size
                self.x = x
            elif len(args) == 4:
                id, size, x, y = args
                self.id = id
                self.size = size
                self.x = x
                self.y = y
        else:
            if kwargs is not None:
                for key in kwargs.keys():
                    if key == 'id':
                        self.id = kwargs[key]
                    elif key == 'width':
                        self.size = kwargs[key]
                    elif key == 'x':
                        self.x = kwargs[key]
                    elif key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """Dictonary representation of the class"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

#!/usr/bin/python3
"""Module to contain the class ``Rectangle``
inheriting from ``Base`` class
"""


from models.base import Base


class Rectangle(Base):
    """Class definintion"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the arguments"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) == int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) == int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle using ``#``"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for a in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """String representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the argument placement"""
        if args is not None and len(args) != 0:
            if len(args) == 1:
                super().__init__(args[0])
            elif len(args) == 2:
                id, width = args
                super().__init__(id)
                self.width = width
            elif len(args) == 3:
                id, width, height = args
                super().__init__(id)
                self.width = width
                self.height = height
            elif len(args) == 4:
                id, width, height, x = args
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
            elif len(args) == 5:
                id, width, height, x, y = args
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y
        else:
            if kwargs is not None:
                for key in kwargs.keys():
                    if key == 'id':
                        super().__init__(kwargs[key])
                    elif key == 'width':
                        self.width = kwargs[key]
                    elif key == 'height':
                        self.height = kwargs[key]
                    elif key == 'x':
                        self.x = kwargs[key]
                    elif key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """Dictonary representation of the class"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

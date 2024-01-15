#!/usr/bin/python3
"""Square module creation"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value
            self.__size = value

    def update(self, *args, **kwargs):
        """Update attributes with arguments"""
        att_list = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x,
                self.y, self.__size)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {'id': self.id, 'x': self.x, 'size': self.__size, 'y': self.y}

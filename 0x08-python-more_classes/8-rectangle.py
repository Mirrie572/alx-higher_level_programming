#!/usr/bin/python3
"""Module with a Rectangle class"""


class Rectangle:
    """
        Rectangle class represents a geometric rectangle.

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
    """
    number_of_instances = 0  # Initialize the class variable
    print_symbol = "#"  # Initialize the class variable

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
                [str(self.print_symbol)
                    * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_first, rect_second):
        if not isinstance(rect_first, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_second, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_first if rect_first.area() >=\
            rect_second.area() else rect_second

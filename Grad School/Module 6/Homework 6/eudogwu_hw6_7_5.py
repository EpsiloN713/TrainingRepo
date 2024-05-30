"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 7.5
Geometry of an n sided polygon
"""
import math


class RegularPolygon:
    """Sets up Polygon object with defaults"""

    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def __str__(self):
        """Print statement for the Polygon Object"""
        return ("The Perimeter is {peri:.2f}, Area is {area:.2f} The x "
                "coordinate "
                "is "
                "{x}, The y coordinate is {y}".format(
            peri=self.get_perimeter(), area=self.get_area(), x=self.__x,
            y=self.__y))

    """Get and set statements for attributes"""

    def get_n(self):
        return self.__n

    def get_side(self):
        return self.__side

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_n(self, n):
        self.__n = n

    def set_side(self, side):
        self.__side = side

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_perimeter(self):
        """Perimeter of the side calculated"""
        return self.get_side() * self.get_n()

    def get_area(self):
        """Area of the side calculated"""
        area = (self.get_n() * (self.get_side() ** 2)) / (4 * math.tan(
            math.pi / self.get_n()))
        return area


if __name__ == '__main__':
    # Test Polygons with printed results
    poly1 = RegularPolygon()
    poly2 = RegularPolygon(6, 4)
    poly3 = RegularPolygon(10, 4, 5.6, 7.8)
    print(poly1)
    print(poly2)
    print(poly3)

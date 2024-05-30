"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 7.1
Creating Rectangle Class
"""


class Rectangle:
    """This Class constructs Rectangle Object and all it's contents"""
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def get_area(self):
        """Calculates area of rectangle"""
        return self.width * self.height

    def get_perimeter(self):
        """Calculates perimeter of rectangle"""
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    # Tests rectangles and prints results
    rect1 = Rectangle(width=4, height=40)
    rect2 = Rectangle(width=3.5, height=35.7)

    print("Rectangle 1 has a width of {}, height of {:,.2f}, area of {:,"
          ".2f} and "
          "perimeter "
          "of {}".format(rect1.width, rect1.height, rect1.get_area(),
                         rect1.get_perimeter()))
    print("Rectangle 2 has a width of {}, height of {:,.2f}, area of {:,"
          ".2f} and "
          "perimeter "
          "of {}".format(rect2.width, rect2.height, rect2.get_area(),
                         rect2.get_perimeter()))

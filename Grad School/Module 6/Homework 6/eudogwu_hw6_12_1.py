"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 7.7
Two by Two linear equations
"""


class GeometricObject:
    """Geometric Object Superclass and defaults"""

    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)


class Triangle(GeometricObject):
    """ Triangle Object subclass with defaults"""

    def __init__(self, side1=1, side2=1, side3=1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __str__(self):
        return "Triangle is {color}, is {filled}, has a perimeter of {" \
               "peri:.2f}, " \
               "and area of {area:.2f}".format(color=self.get_color(),
                                               filled=self.is_filled(),
                                               peri=self.get_perimeter(),
                                               area=self.get_area())

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def get_area(self):
        """Calculates area of triangle"""
        return (self.get_s() * (self.get_s() - self.__side1) * (self.get_s() -
                                                                self.__side2) * (
                        self.get_s() - self.__side3)) ** 0.5

    def get_s(self):
        """ gets S for area calculation"""
        return (self.__side1 + self.__side2 + self.__side3) / 2

    def get_perimeter(self):
        """Calculates perimeter of triangle"""
        return self.__side1 + self.__side2 + self.__side3


if __name__ == '__main__':
    # Get input from user and validates it
    LIST_SIZE = 3
    while True:
        user_input_list = input(
            'Enter {0} numbers for side 1, side 2, and side3, '
            'separated '
            'by '
            'commas: '.
                format(LIST_SIZE)).split(',')
        if len(user_input_list) != LIST_SIZE:
            print('You did not enter {0} numbers separated by commas'.format(
                LIST_SIZE))
            next
        try:
            for x in range(LIST_SIZE):
                user_input_list[x] = float(user_input_list[x])
            break
        except:
            print('{0} is not a float number. Please try again'.format(x))

    # Pull values from input list
    side1_input = user_input_list[0]
    side2_input = user_input_list[1]
    side3_input = user_input_list[2]

    # Inputs values and prints results
    triangle_input = Triangle(side1_input, side2_input, side3_input)
    color = input("Enter Triangle Color: ")
    triangle_input.set_color(color)
    filled2 = input("Enter 1 to fill or 0 to not fill: ")
    color_filled = (filled2 == 1)
    triangle_input.set_filled(color_filled)
    print(triangle_input)

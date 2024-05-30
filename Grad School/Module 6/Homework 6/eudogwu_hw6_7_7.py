"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 7.7
Two by Two linear equations
"""


class LinearEquation:
    """Sets up Linear equation object with defaults"""
    def __init__(self, a, b, c, d, e, f, ):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def __str__(self):
        """Prints out statement describing Object"""
        if self.is_solvable():
            return "The X coordinate is {x} and the Y coordinate is {y}" \
                .format(x=self.get_x(), y=self.get_y())
        else:
            return "The Equation has no solution"

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f
    """Gets denominator for calculations"""
    def get_denominator(self):
        return (self.__a * self.__d) - (self.__b * self.__c)

    def is_solvable(self):
        if self.get_denominator() != 0:
            return True

    def get_x(self):
        """Calculates X"""
        return ((self.__e * self.__d) - (self.__b * self.__f)) / (
            self.get_denominator())

    def get_y(self):
        """Calculates Y"""
        return ((self.__a * self.__f) - (self.__e * self.__c)) / (
            self.get_denominator())


if __name__ == '__main__':
    LIST_SIZE = 6
    while True:
        # Gets input and validates it
        user_input_list = input(
            'Enter {0} numbers for a, b, c, d, e, f, separated '
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
    a_input = user_input_list[0]
    b_input = user_input_list[1]
    c_input = user_input_list[2]
    d_input = user_input_list[3]
    e_input = user_input_list[4]
    f_input = user_input_list[5]
# Plugs values in and prints results
    equation = LinearEquation(a_input, b_input, c_input, d_input, e_input,
                              f_input)
    print(equation)

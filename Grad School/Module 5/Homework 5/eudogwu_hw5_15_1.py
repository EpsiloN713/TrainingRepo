"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 15.1
Sum the Digits in an integer using recursion
"""


def sum_digits(n):
    """Recursive Function that adds remainders and loops back until there is
    none"""
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


if __name__ == '__main__':

    import sys

    # Get Input from user
    user_input = int(input("Enter a positive number and the sum of the numbers "
                           "will be returned: "))
    # Check if input is Integer
    try:
        inp_num = int(user_input)
    except:
        print('Not a valid integer!')
        sys.exit()
    # Check if input is positive
    if user_input < 0:
        print("Not a Positive Number!")
        sys.exit()

    print("The Sum of the Digits are: ", sum_digits(user_input))

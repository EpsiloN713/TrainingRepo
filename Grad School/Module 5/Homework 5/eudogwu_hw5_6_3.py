"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 6.3
Get user input and determine if it is a palindrome
"""


# Define reverse and Palindrome Functions
def reverse(number):
    """Function that reverses a string and returns the result"""
    result = ''
    for i in range(len(number), 0, -1):
        result += number[i - 1]
    return result


def is_palindrome(n):
    """Function that checks if string is a palindrome by checking with
    reverse function. Needs to be used in conjunction with reverse function"""
    if n == reverse(n):
        return True
    else:
        return False


if __name__ == '__main__':
    import sys

    # Get User input and check if it is the correct kind of input
    user_input = input('Enter an integer to check if it is a palindrome: ')
    try:
        inp_num = int(user_input)
    except:
        print('Not a valid integer!')
        sys.exit()
    # Convert input to string and check if it is a palindrome and print results
    s = str(user_input)
    if is_palindrome(s):
        print("{} is a Palindrome".format(user_input))
    else:
        print("{} is not a Palindrome".format(user_input))

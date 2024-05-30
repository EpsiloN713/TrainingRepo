"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 6.5
Sort Three Numbers
"""


# Define Function
def sort_numbers(a, b, c):
    """Function to Sort Three Numbers and return three sorted numbers"""
    num1 = min(a, b, c)
    num3 = max(a, b, c)
    num2 = (a + b + c) - num1 - num3
    return num1, num2, num3


if __name__ == '__main__':
    LIST_SIZE = 3
    # Checks Input to see if the correct values are entered
    while True:
        user_input_list = input(
            'Enter {0} numbers separated by commas and they '
            'will be sorted: '.
                format(LIST_SIZE)).split(',')
        if len(user_input_list) != LIST_SIZE:
            print(
                'You did not enter {0} items separated by commas'.format(
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

    print("The Sorted Numbers are: {}".format(sort_numbers(a_input, b_input,
                                                           c_input)))

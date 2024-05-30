"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 6.1
Compute pentagonal numbers
"""


def get_pentagonal_number(n):
    """Function calculates the pentagonal number and returns the value"""
    result = n * (3 * n - 1) // 2
    return result


if __name__ == '__main__':
    # Set Number count to zero
    test_num = 0
    # Displays 10 numbers per line
    NUMBER_OF_FACTS_PER_LINE = 10

    # Prints results of the function calculation at 10 per line and increases
    # count
    while test_num < 100:
        test_num += 1
        print(format(get_pentagonal_number(test_num), "10d"), end='')
        if test_num % NUMBER_OF_FACTS_PER_LINE == 0:
            print()

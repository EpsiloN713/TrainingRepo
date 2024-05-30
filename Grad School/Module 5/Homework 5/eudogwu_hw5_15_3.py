"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 15.3
Compute greatest common divisor using recursion using recursion
"""


# Define GCD Function
def gcd(m, n):
    """Recursive Function that calculates the Greatest Common Denominator and
    stops when % is zero """
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


if __name__ == '__main__':
    import sys

    # Get inputs from user
    num_a = int(input("Enter first number:"))
    try:
        inp_num = int(num_a)
    except:
        print('Not a valid integer!')
        sys.exit()
    num_b = int(input("Enter second number:"))
    try:
        inp_num = int(num_b)
    except:
        print('Not a valid integer!')
        sys.exit()

    greatest_com_dom = gcd(num_a, num_b)
    print("The GCD of {} and {} is: {}" .format(num_a, num_b, greatest_com_dom))

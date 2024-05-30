"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 1 2019
Homework Problem: 1.7
Calculate approximate Pi.
"""
# set approx_pi to equation
approx_pi1 = 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11)
approx_pi2 = 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15)
print("Calculating Problem 1... ")  # Tell User What program is doing
print("The answer is : {}".format(approx_pi1))  # Print Result to user
print("Calculating Problem 2... ")  # Tell User What program is doing
print("The answer is : {}".format(approx_pi2,))  # Print Result to user

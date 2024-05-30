"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 16 2019
Homework Problem: 5.1
Use user input to count positive and negative numbers and compute average
numbers
"""
import sys

# Positive, Negative and Number of Units Count
pos_num_count = 0
neg_num_count = 0
unit_count = 0
# Sum of inputs variable
total_number = 0
# Declared user input as a None Type to be able to use it
user_inp = None
while user_inp != 0:
    # Get input from user and validate
    user_inp = input('Enter an integer, the input ends if it is 0: ')
    try:
        inp_num = int(user_inp)
    except:
        print('Not a valid integer!')
        sys.exit()
    # Sets up break if user types zero
    if inp_num == 0:
        break
    # Sets up counts for positive, negative, total, and unit counts
    elif inp_num > 0:
        pos_num_count += 1
        total_number += inp_num
        unit_count += 1
    else:
        neg_num_count += 1
        total_number += inp_num
        unit_count += 1
    # Assign average variable
    average = total_number / unit_count
# When user enters zero, this is where loop breaks to and prints message
if unit_count == 0:
    print("You didn't enter any number, program terminated")
# Results are printed here for all other situations
else:
    print("The Number of positives is: {}".format(pos_num_count))
    print("The Number of negatives is: {}".format(neg_num_count))
    print("The total is: {}".format(unit_count))
    print("The average is: {}".format(average, ".2f"))

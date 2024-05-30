"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 11.1
Sum of elements from a matrix column
"""
import sys

# Create empty list for table
matrix = []

# set row count to zero
row_count = 0

# loop to continue asking for input
while len(matrix) < 3:
    user_inp = input('Enter a 3-by-4 matrix row for row {} seperated by '
                     'spaces: '.format(
        row_count)).split()
    if len(user_inp) != 4:
# Error message when incorrect digits are entered
        print("You did Not enter 4 digits")
        sys.exit()
    for l in range((len(user_inp))):
        try:
            user_inp[l] = float(user_inp[l])
        except:
            print('{} is not a float!'.format(user_inp[l]))
            sys.exit()
# sets up matrix from user input value and calculates sum
    matrix.append(user_inp)
    row_count += 1
for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
# Print results
    print("Sum for column", column, "is", total)
print(matrix)

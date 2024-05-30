"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 10.5
Print Distinct numbers from input
"""
import sys

# Make list for distinct Numbers
dis_list = []
# Get user input and check if the input is the correct amount
list = input('Enter ten Numbers separated by spaces: ').split()
if len(list) != 10:
    print("You did not enter 10 numbers")
    sys.exit()
# Convert input to integer
for l in range(len(list)):
    try:
        list[l] = int(list[l])
    except:
        print('{} is not a integer!'.format(list[l]))
        sys.exit()
for i in list:
    # Adds distinct numbers to list
    if i not in dis_list:
        dis_list.append(i)
# Prints Distinct number results
print("The Distinct numbers are: ", end='')
print(*dis_list)

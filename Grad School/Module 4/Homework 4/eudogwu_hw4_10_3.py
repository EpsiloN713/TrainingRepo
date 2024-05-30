"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 10.1
Count the Occurrences of numbers
"""
import sys
# Prompt fr inputs
list = input('Enter integers between 1 and 100: ').split()
# Convert inputs to integers
for l in range(len(list)):
    try:
        list[l] = int(list[l])
    except:
        print('{} is not a integer!'.format(list[l]))
        sys.exit()
# Check if number is in range
for s in list:
    if s >= 100:
        print('A number is above the asked range')
        sys.exit()
    if s <= 1:
        print('A number is below the asked range')
        sys.exit()
# Create empty list for distinct numbers
dup_list = []

# Scans List and counts the numbers in list
for number in list:
    list.count(number)
    if list.count(number) > 1:
        print("{} occurs {} times".format(number, list.count(number)))
    else:
        print("{} occurs {} time".format(number, list.count(number)))

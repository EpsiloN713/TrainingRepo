"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 16 2019
Homework Problem: 5.3
Check Social Security Numbers
"""
# User input received
ss_number = input("enter SSN (in format: ddd-dd-dddd): ")
# Splits at dash and places in a list
ss_list = ss_number.split('-')
# Replaces dashes from input with no spaces
ss_whole = ss_number.replace('-', '')
# Social security number character count
ss_count = 0

# Intention was for when number count is not 9 it will continue loop
while ss_count != 9:
    # This is supposed to check if the format of the input is correct
    if len(ss_list[0]) != 3 or len(ss_list[1]) != 2 or len(ss_list[2]) != 4:
        print("Not a Valid SS number")
        break
    # If the format is correct it would continue the program
    elif len(ss_list[0]) == 3 or len(ss_list[1]) == 2 or len(ss_list[2]) == 4:
        # It would go through the characters and check if they are numbers
        for num_count in ss_whole:
            if num_count.isdigit():
                # each time it finds a number it will count
                ss_count += 1
            elif num_count.isalpha():
                break
            elif num_count.isspace():
                break
            # When count reaches nine it will say it is valid
            if ss_count == 9:
                print("Valid SS Number")
else:
    print("Not a Valid SS number")

"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 10.1                      
Assign grades from input
"""
import sys
# Get User input and convert into float
grades = input('Enter scores: ').split()
for l in range(len(grades)):
    try:
        grades[l] = float(grades[l])
    except:
        print('{} is not a float!'.format(grades[l]))
        sys.exit()
# Statements to check the grades and assign scores to students and print results
for number in grades:
    if number >= max(grades) - 10:
        print("Student {} score is {} and the grade is A".format(
            grades.index(number), number))
    elif number >= max(grades) - 20:
        print("Student {} score is {} and the grade is B".format(
            grades.index(number), number))
    elif number >= max(grades) - 30:
        print("Student {} score is {} and the grade is C".format(
            grades.index(number), number))
    elif number >= max(grades) - 40:
        print("Student {} score is {} and the grade is D".format(
            grades.index(number), number))
    else:
        print("Student {} score is {} and the grade is F" .format(
            grades.index(number), number))

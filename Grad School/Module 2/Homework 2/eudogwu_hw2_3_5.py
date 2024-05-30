"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 3.5
Use user input to calculate the area of a regular polygon
"""

# Import Math
import math

# Prompt user to input the number of sides
num_sides = eval(input("Enter the number of sides: "))

# Prompt user to input the length of sides
len_sides = eval(input("Enter the length of the sides: "))

# Calculate the area

area = (num_sides * (len_sides **2)) / (4 * math.tan(math.pi / num_sides))

# Display Results
print("The Area of the polygon is {}" .format(format(area, ".2f")))
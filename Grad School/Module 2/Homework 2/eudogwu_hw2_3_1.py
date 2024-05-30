"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 3.1
Calculate The Area of a pentagon
"""
# import math module to use the math functions
import math

# Get radius from user input
radius = eval(input("Enter the length from the center to vertex: "))

# Calculate side
side = 2 * radius * math.sin(math.pi / 5)

# Calculate area
area = ((3 * math.sqrt(3)) / 2) * side ** 2

# Display Results
print("The area of the pentagon is {}" .format(format(area, ".2f")))

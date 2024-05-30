"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 1 2019
Homework Problem: 1.9
(Area and perimeter of a rectangle) Write a program that displays the area and
perimeter of a rectangle with the width of 4.5 and height of 7.9
"""
width = 4.5  # Set width
height = 7.9  # Set height
area = width * height  # Set Area with Equation
perimeter = 2 * (width + height)  # Set Perimeter with Equation
print("Calculating Area and perimeter of Rectangle")
print("Area of Rectangle with width {} and height {} " \
      "is: {}".format(width, height, format(area, "3.2f")))
print("Perimeter of Rectangle with width {} and height {} " \
      "is: {}".format(width, height, perimeter))

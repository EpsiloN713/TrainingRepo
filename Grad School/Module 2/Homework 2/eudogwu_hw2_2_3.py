"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 2.3
Convert Feet to Meters
"""

# Prompt user for Feet Measurement input
feet = eval(input("Enter a value for feet: "))
# Calculate meters by multiplying by given meters conversion factor
meters = feet * .305
# Display Results
print("{} feet is {} meters" .format(feet, meters))


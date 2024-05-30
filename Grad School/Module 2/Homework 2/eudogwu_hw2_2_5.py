"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 2.5
Calculate Gratuity and Total from user inputs
"""
# Get subtotal and gratuity from user and assign to variables
subtotal, gratuity = eval(input("Enter the Subtotal and a Gratuity rate "
                                "separated by a comma: "))
# Convert gratuity to to decimal and assign to new variable
percent = gratuity / 100
# Calculate tip amount
tip_amount = percent * subtotal
# Calculate the total of the subtotal and tip amount
total_amount = tip_amount + subtotal
# Display Results
print("The gratuity is {}{} and the total is {}{}" .format("$", format(
    tip_amount, ".2f"), "$", format(total_amount, ".2f")))



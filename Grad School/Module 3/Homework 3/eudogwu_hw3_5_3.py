"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 16 2019
Homework Problem: 5.3
Display chart that converts kilograms to pounds
"""
# Constant to divide pounds By
KG_CONVERSE = 0.45359237
# Set Max number of times to convert
NUMBER_OF_KG = 200
# Kilos counter, Goes up each loop
kilos = 0
# Initial print statement
print("Kilograms      Pounds")
# Loop that tests if number is Odd, when odd it calculates pounds. Limit is set
while kilos < NUMBER_OF_KG:
    kilos += 1
    if kilos % 2 != 0:
        pounds = kilos / KG_CONVERSE
# Print Results
        print("{}               {:,.1f}".format(kilos, pounds))


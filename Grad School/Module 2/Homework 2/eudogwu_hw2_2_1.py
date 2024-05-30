"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 2.1
Convert Celsius to Fahrenheit
"""

# Note: Unicode for Degrees is "\u00b0". Assign to Variable for ease of use
deg_sym = "\u00b0"
# Prompt user to enter celsius input
celsius = eval(input("Enter a degree in celsius: "))
# Calculate Fahrenheit
fahrenheit = (9 / 5) * celsius + 32
# Display Results
print("{}{} Celsius is {}{} Fahrenheit"
      .format(format(celsius, ".1f"), deg_sym, format(fahrenheit, ".1f"),
              deg_sym))

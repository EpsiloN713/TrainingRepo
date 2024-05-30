"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 16 2019
Homework Problem: 4.1
Use user input to solve quadratic equations
"""
import math
LIST_SIZE = 3
# Checks Input to see if the correct values are entered
while True:
    user_input_list = input('Enter {0} numbers for a, b, and c separated by '
                            'commas: '.
                            format(LIST_SIZE)).split(',')
    if len(user_input_list) != LIST_SIZE:
        print(
            'You did not enter {0} items separated by commas'.format(LIST_SIZE))
        next
    try:
        for x in range(LIST_SIZE):
            user_input_list[x] = float(user_input_list[x])
        break
    except:
        print('{0} is not a float number. Please try again'.format(x))

# Pull values from input list
a_input = user_input_list[0]
b_input = user_input_list[1]
c_input = user_input_list[2]

# Calculate Discriminant
discrim = (b_input ** 2 - 4 * a_input * c_input)

# Positive Discriminant calculations and Print Results
if discrim > 0:
   sqdiscrim = math.sqrt(discrim)
   root1 = (-1 * b_input + sqdiscrim) / 2 * a_input
   root2 = (-1 * b_input - sqdiscrim) / 2 * a_input
   print("The roots are {:,.2f} and {:,.2f}".format(root1, root2))
# Calculate Zero Discriminant and Print Results
elif discrim == 0:
   sqdiscrim = math.sqrt(discrim)
   root1 = (-1 * b_input + sqdiscrim) / 2 * a_input
   print("The root is {}".format(root1, ".2f"))
else:
   print("The equation has no real roots")

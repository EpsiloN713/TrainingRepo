"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 16 2019
Homework Problem: 4.3
Use user input to solve 2 x 2 linear equations
"""
LIST_SIZE = 6
while True:
    user_input_list = input('Enter {0} numbers for a, b, c, d, e, f, separated '
                            'by '
                            'commas: '.
                            format(LIST_SIZE)).split(',')
    if len(user_input_list) != LIST_SIZE:
        print('You did not enter {0} numbers separated by commas'.format(
                LIST_SIZE))
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
d_input = user_input_list[3]
e_input = user_input_list[4]
f_input = user_input_list[5]

# Calculate Denominator
denom = (a_input * d_input) - (b_input * c_input)

# Runs calculations as long as the Denominator is NOT Zero
if denom != 0:
    x_cord = ((e_input * d_input) - (b_input * f_input)) / (denom)
    y_cord = ((a_input * f_input) - (e_input * c_input)) / (denom)
# Display results
    print("x is {:,.1f} and y is {:,.1f}" .format(x_cord,y_cord))
else:
    print("The Equation has no solution")

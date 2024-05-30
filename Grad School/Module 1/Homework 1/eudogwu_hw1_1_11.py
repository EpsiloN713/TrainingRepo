"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 1 2019
Homework Problem: 1.11
Calculate and display population for next 5 years
"""

current_pop = 312032486
year_seconds = 31536000
total_born = year_seconds // 7
total_dead = year_seconds // 13
total_imm = year_seconds // 45
total_pop = current_pop + total_born + total_imm - total_dead

# Display result for Year 1
print("The Current Population is: {}" .format(current_pop))
print("After Year 1, The population will be: {}" .format(total_pop))
print("...")

# Make current population equal to total population
current_pop = total_pop
#Calculate Total Population Again
total_pop = current_pop + total_born + total_imm - total_dead
# Display result for Year 2
print("The Current Population is: {}" .format(current_pop))
print("After Year 2, The population will be: {}" .format(total_pop))
print("...")

# Make current population equal to total population
current_pop = total_pop
#Calculate Total Population Again
total_pop = current_pop + total_born + total_imm - total_dead
# Display result for Year 3
print("The Current Population is: {}" .format(current_pop))
print("After Year 3, The population will be: {}" .format(total_pop))
print("...")

# Make current population equal to total population
current_pop = total_pop
#Calculate Total Population Again
total_pop = current_pop + total_born + total_imm - total_dead
# Display result for Year 4
print("The Current Population is: {}" .format(current_pop))
print("After Year 4, The population will be: {}" .format(total_pop))
print("...")

# Make current population equal to total population
current_pop = total_pop
#Calculate Total Population Again
total_pop = current_pop + total_born + total_imm - total_dead
# Display result for Year 5
print("The Current Population is: {}" .format(current_pop))
print("After Year 5, The population will be: {}" .format(total_pop))
print("...")
"""
Marc Lowenthal
Class: CS 521
Date: 12/4/2019
Example using Mug.py
"""

# Import CLASS Mug from FILE Mug.py
from Mug import Mug

if __name__ == '__main__':

    # instantiate mug object
    marc_mug = Mug('clear', contents='beer',  material='glass')

    # set temperature
    marc_mug.set_temp(50)

    print(marc_mug)

    # Convert the result to a string,
    # get the length of the string, find the integer of 1/2 the length and
    # finally, multiply it by a two character line.
    print('=-' * int(round(len(str(marc_mug))/2,0)))

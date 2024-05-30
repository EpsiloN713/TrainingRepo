"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Final Project
IP Address analyzer
"""

import sys
import os
from netfile import wildcard
from netfile import Net_Check

if __name__ == '__main__':

    # Empty Wildcard List used
    ip_wild_list = []
    # Gets input from user and validates
    ip_user_inp = input(
        "Enter IP address in XXX.XXX.XXX.XXX format, each section "
        "is between 0 and 255: ").split(
        ".")
    if len(ip_user_inp) != 4:
        print("You did not enter in XXX.XXX.XXX.XXX format")
        sys.exit()

    # Convert input to integer
    for l in range(len(ip_user_inp)):
        try:
            ip_user_inp[l] = int(ip_user_inp[l])
        except:
            print('{} is not a integer!'.format(ip_user_inp[l]))
            sys.exit()

    # Checks if a valid IP address was inputted
    for item in ip_user_inp:
        if item > 255 or item < 0:
            print("Not a valid IP address, all octets must be between 0 and 255"
                  .format())
            sys.exit()

    # Creates Wildcard List by using function to subtract 255 from octet
    for ip_oct in ip_user_inp:
        ip_wild_list.append(wildcard(ip_oct))

    # Print out results
    print("The IP Address is {}".format('.'.join(map(str, ip_user_inp))))
    print("The Wildcard mask is {}".format('.'.join(map(str,
                                                            ip_wild_list))))
    print(Net_Check(ip_user_inp[0]))

    # Open files to read lines
    file_read = open('projectfile.txt', "r")
    # Reads lines and prints possible hosts from file
    lines = file_read.readlines()
    if ip_user_inp[0] in range(1, 126):
        print(lines[0])
    elif ip_user_inp[0] in range(128, 191):
        print(lines[1])
    elif ip_user_inp[0] in range(192, 223):
        print(lines[2])
    else:
        print(lines[3])
    file_read.close()

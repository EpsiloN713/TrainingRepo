"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 30 2019
Homework Problem: 6.9
Convert between feet and meters
"""


def foot_to_meter(foot):
    """Function to convert feet to meters"""
    return foot * .3048


def meter_to_foot(meter):
    """Function to convert meters to feet"""
    return meter * 3.2808


if __name__ == '__main__':
    # Print headers and separators
    print(format("Feet", "<15s"), format("Meters", "<15s"), "  |    ", format(
        "Meters", "<15s"), format("Feet", "<15s"))
    print("---------------------------------------------------------------")

    # Set up Counters for feet and meters
    foot = 1
    meter = 20
    count = 1

    # Prints out Conversions in a table and increments accordingly
    while count <= 10:
        print(format(foot, "<15d"),
              format(foot_to_meter(foot), "<15.3f"), "  |    ",
              format(meter, "<15d"),
              format(meter_to_foot(meter), "<15.3f"))
        foot += 1
        meter += 5
        count += 1

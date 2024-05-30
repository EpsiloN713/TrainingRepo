"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 3.2
calculating distance
"""
import math

lat1, long1 = eval(input("Enter point one: "))
radlat1, radlong1 = math.radians(lat1), math.radians(long1)
lat1, long1 = radlat1, radlong1

lat2, long2 = eval(input("Enter point two: "))
radlat2, radlong2 = math.radians(lat2), math.radians(long2)
lat2, long2 = radlat2, radlong2

radius = 6371.01

distance = radius * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(
    lat1) * math.cos(lat2) * math.cos(long1 - long2))

print("The distance is {}" .format(distance))
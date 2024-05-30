"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 8 2019
Homework Problem: 3.3
Calculate The Area enclosed by four cities
"""
import math

# Set Earth's radius as the radius
radius = 6371

# convert ATL lat and long to radians
atl_lat, atl_long = 33.6394444444, -84.4280555556
rad_atl_lat, rad_atl_long = math.radians(atl_lat), math.radians(atl_long)
atl_lat, atl_long = rad_atl_lat, rad_atl_long

# convert CLT lat and long to radians
clt_lat, clt_long = 35.2138888889, -80.9430555556
rad_clt_lat, rad_clt_long = math.radians(clt_lat), math.radians(clt_long)
clt_lat, clt_long = rad_clt_lat, rad_clt_long

# convert SAV lat and long to radians
sav_lat, sav_long = 32.1275, -81.20194
rad_sav_lat, rad_sav_long = math.radians(sav_lat), math.radians(sav_long)
sav_lat, sav_long = rad_sav_lat, rad_sav_long

# convert MCO lat and long to radians
mco_lat, mco_long = 28.4286111111, -81.3086111111
rad_mco_lat, rad_mco_long = math.radians(mco_lat), math.radians(mco_long)
mco_lat, mco_long = rad_mco_lat, rad_mco_long

# Calculate distance of SIDE ONE ATL - CLT
distance_side1 = radius * math.acos(math.sin(atl_lat) * math.sin(clt_lat) +
                                    math.cos(atl_lat) * math.cos(clt_lat) *
                                    math.cos(atl_long - clt_long))

# Calculate distance of SIDE TWO CLT - SAV
distance_side2 = radius * math.acos(math.sin(clt_lat) * math.sin(sav_lat) +
                                    math.cos(clt_lat) * math.cos(sav_lat) *
                                    math.cos(clt_long - sav_long))

# Calculate distance of SIDE THREE ATL - SAV
distance_side3 = radius * math.acos(math.sin(atl_lat) * math.sin(sav_lat) +
                                    math.cos(atl_lat) * math.cos(sav_lat) *
                                    math.cos(atl_long - sav_long))

# Calculate distance of SIDE FOUR SAV - MCO
distance_side4 = radius * math.acos(math.sin(sav_lat) * math.sin(mco_lat) +
                                    math.cos(sav_lat) * math.cos(mco_lat) *
                                    math.cos(sav_long - mco_long))

# Calculate distance of SIDE FIVE ATL - MCO
distance_side5 = radius * math.acos(math.sin(atl_lat) * math.sin(mco_lat) +
                                    math.cos(atl_lat) * math.cos(mco_lat) *
                                    math.cos(atl_long - mco_long))

# calculate the sides of triangle1
triangle_s1 = (distance_side1 + distance_side2 + distance_side3) / 2

# calculate the area1
area1 = (triangle_s1 * (triangle_s1 - distance_side1) *
         (triangle_s1 - distance_side2) *
         (triangle_s1 - distance_side3)) ** 0.5

# calculate the sides of triangle2
triangle_s2 = (distance_side3 + distance_side4 + distance_side5) / 2

# calculate the area2
area2 = (triangle_s2 * (triangle_s2 - distance_side3) *
         (triangle_s2 - distance_side4) *
         (triangle_s2 - distance_side5)) ** 0.5

# Calculate the area of the
area_whole = area1 + area2

# Print results
print("The area between Atlanta, Charlotte, "
      "Orlando and Savannah is: {} km" .format(format(area_whole, ".2f")))

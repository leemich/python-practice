#!/usr/bin/python

# This script will find the area of a circle given user input

#Set the value of pi
pi = 3.14159

# Ask the user to input the radius of the circle and convert to float
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and print the result
area = pi * (radius ** 2)

print()
print("The area of the circle is:", area)

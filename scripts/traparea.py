#!/usr/bin/python
# Script to find the area of a trapezoid based on user input

# Print the purpose of the script
print("Find the area of a trapezoid.")
print()

#Ask user for height and lengths of trapezoid and convert input to floats
trap_height = float(input("Enter the height of the trapezoid: "))
bot_base = float(input("Enter the length of the bottom  base: "))
top_base = float(input("Enter the length of the top base: "))

# Find the area using standard formula

trap_area = ((bot_base + top_base) / 2) * trap_height

# Print the result to the screen
print()
print("The area of the trapezoid is", trap_area)
             

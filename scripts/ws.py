#!/usr/bin/python

# This script converts the temperature from Fahrenheit to Celsius

# Ask user for Far. temp and convert the input into a floating point number
far_temp = float(input("Enter the temperature in Fahrenheit: "))

# Convert to Celsius by subtracting 32 and then multiplying by 5/9
cel_temp = (far_temp - 32) * (5 / 9)

# Print a blank line for readabilty
print()

# Print the value of cel_temp to the screen
print("The temperature in Celsius is", cel_temp)

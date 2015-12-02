# Coding challenge #3
#
# Create a script that takes user input for the length of
# three sides of a triangle and check to see if they form
# a right triangle
#
# a sqaured + b squared == c squared
# hypotenous (c) is always the longest side

def check_sides():
    print('Please enter the length of side 1:')
    side1 = float(input('> '))
    print()
    print('Please enter the length of side 2:')
    side2 = float(input('> '))
    print()
    print('Please enter the length of side 3:')
    side3 = float(input('> '))
    sidelist = [side1, side2, side3]
    sidelist.sort()
    a = sidelist[0]
    b = sidelist[1]
    c = sidelist[-1]
    if (a ** 2) + (b ** 2) == (c ** 2):
        print('The triangle is a right triangle.')
    else:
        print('The triangle is not a right triangle.')
    

print('''
This program will tell you if a given triangle is a right triangle
or not given the length of each  of the sides.

''')

while True:
    print()
    print('Would you like to evaluate a triangle? Y/N:')
    response = input('> ')
    if response.lower() == 'n':
        print('Thanks for playing!')
        break
    check_sides()

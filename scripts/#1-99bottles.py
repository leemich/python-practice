#!/usr/bin/python
# Coding challenge #1
#
# Write a python scripts that prints out the lyrics
# of 99 Bottles of Beer on the Wall


for i in range(99, 0, -1):
    if i == 1:
        print(str(i) + ' bottle of beer on the wall, ' + str(i) + ' bottle of beer.')
        print('Take one down, pass it around, ' + str(i -1) + ' bottles of beer on the wall.')
        break
    i +- 1          
    print(str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.')
    print('Take one down, pass it around, ' + str(i - 1) + ' bottles of beer on the wall.')
    print()      
    


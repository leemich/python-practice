#!/usr/bin/python
#
# Coding challenge - find the number with the following qualities:

# Between 1 and 1000, there is only 1 number that meets the following criteria. While it could be manually figured out with pen and paper, it would be much more efficient to write a program that would do this for you. With that being said, your goal is to find out which number meets these criteria. To find out if you have the correct number, click the link at the bottom of this main post.

#     The number has two or more digits.

#     The number is prime.

#     The number does NOT contain a 1 or 7 in it.

#     The sum of all of the digits is less than or equal to 10.

#     The first two digits add up to be odd.

#     The second to last digit is even and is NOT zero.

#     The last digit is equal to how many digits are in the number.

#	  Should return the number 523


# Function to check if number is prime

def check_prime(num):
	factor_list = []
	for i in range(1, num + 1):
		if num % i == 0:
			factor_list.append(i)
	if len(factor_list) == 2:
		return True

# Make sure the number does not contain a 1 or a 7

def no1or7(num):
	if '1' not in str(num) and '7' not in str(num):
		return True

# Check to see if sum of all digits <= 10

def digit_sum(num):
	numsum = sum(int(x) for x in str(num))
	if numsum <= 10:
		return True

# Check that 1st two digits add up to an odd number
# AND the second to last number is even and not zero
# AND check that the last digit is equal to the length 
# of the number in digits
#
# Doing these together since they can all be evaluated from
# the same list

def add_odd(num):
	if len(str(num)) >= 3:
		numlist = []
		for char in str(num):
			numlist.append(char)
		two_sum = int(numlist[0]) + int(numlist[1])
		if two_sum % 2 != 0 and int(numlist[-2]) % 2 == 0 and int(numlist[-2]) != 0 and int(numlist[-1]) == len(numlist):
			return True

# Call the functions and print the number that satisfies all conditions

for num in range(1, 1000):
 	if check_prime(num) and no1or7(num) and digit_sum(num) and add_odd(num):
 		print(num)

	



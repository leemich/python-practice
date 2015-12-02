#!/usr/bin/python
#
# define a fucntion that determines if a given number is prime

def check_prime(num):
	factor_list = []
	for i in range(1, num + 1):
		if num % i == 0:
			factor_list.append(i)
	if len(factor_list) == 2:
		print(str(num) + ' is prime.')
	else:
		print(str(num) + ' is not prime.')


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

non_prime_list = [4, 6, 8, 10, 12]

for i in prime_list:
	check_prime(i)

for i in non_prime_list:
	check_prime(i)


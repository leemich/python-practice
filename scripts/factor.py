#!/usr/bin/python
#
# Coding Challenge - define a function that returns
# a list of all factors of a given number including 1 and num
# sorted numerically in ascending order

def factor(num):
	factor_list = []
	for i in range(1, (num + 1)):
		if num % i == 0:
			factor_list.append(i)
	print(factor_list)			

factor(36)
factor(186)
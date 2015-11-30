#!/usr/bin/python
#
# Coding Challenge - Fibonacci Sequence
#
#Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.

def fib_seq():
	x = 0
	y = 1
	print('Enter the length of the sequence:')
	seq_len = int(input('> '))
	if x == 0 and y == 1:
		print(x)
		print(y)
	for i in range(seq_len - 2):
		z = x + y
		print(z)
		x = y
		y = z

fib_seq()


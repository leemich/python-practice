# Coding challenge - Change Calculator

# BASIC GOAL Imagine that your friend is a cashier, but has a hard time counting back change to customers. Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.

# For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

# SUBGOALS

#     So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.

#     To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

print('This program will take the cost of an item, the total cash tendered, and return the amount of change to give back, and the exact amount of coins that make up that change.')

def(change_amt):
	print('Enter the cost of the item:')
	item_cost = float(input('> '))
	print()
	print('Enter cash tendered:')
	amt_paid = float(input('> '))
	global chgret
	chgret = amt_paid - item_cost
	print('Change due: ' + str(chgret))
	return chgret

def(calc_coins):
	


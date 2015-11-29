#!/usr/bin/python
# Coding challenge - Mean Median Mode
#
# Write three functions that allow the user
# to find the mean, median, and mode of a list
# of numbers
#
# Mean - the average
# Median - number in the middle of a list arranged
# from highest to lowest
# Mode - the number that occurs the most

# import collections module in order to use Counter method
import collections

def find_mean(numlist):
	mean = round(sum(numlist) / len(numlist))
	return mean

# NOTE: sorted(list) returns a new list
# list.sort() modifies list in place

def find_median(numlist):
	sorted_list = sorted(numlist)
	median = sorted_list[int((len(numlist) / 2))]
	return median

def find_mode(numlist):
	c = collections.Counter(numlist)
	lmode = [x[0] for x in c.most_common(1)]
	mode = str(lmode[0])
	return mode



mynumlist = [24, 15, 16, 16, 32, 78]
print(find_mean(mynumlist))
print()
print(find_median(mynumlist))
print()
print(find_mode(mynumlist))
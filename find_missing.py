#!/usr/bin/python
'''
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: Exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing (list) , list will always be atleast 3 numbers.

http://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

'''


def find_missing(sequence):
	should = 1.0 * (sequence[0] + sequence[-1])* (len(sequence)+1) / 2
	actual = reduce(lambda x, y: x+y, sequence)
	#print actual
	return int(should - actual)

a = [1, 2, 3, 4, 6, 7, 8, 9]
print find_missing(a)
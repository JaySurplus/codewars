"""
Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

You have to validate input:

v can be anything (primitive or otherwise)
if v is ommited, fill the array with undefined
if n is 0, return an empty array
if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.

	see: http://www.codewars.com/kata/54129112fb7c188740000162/train/python

"""

def prefill(n,v=None):
    #your code here
    try:
    	if isNumber(n):
    		if v is None:
    			return ['undefined'] * int(n)
    		return [v]*int(n)
    	raise TypeError
    except TypeError:
    	return str(n) + " is invalid."


def isNumber(n):
	if isinstance( n, int ):
		return True
	elif isinstance( n , str) and n.isdigit():
		if int(n):
			return True
	return False



	
print prefill(5,)
print prefill(5,prefill(3,'abc'))
print prefill(3,5)

print isNumber(5.3)


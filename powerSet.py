'''

http://www.codewars.com/kata/53d3173cf4eb7605c10001a8/train/python

Write a function that returns all of the sublists of a list or Array.
Your function should be pure; it cannot modify its input.

Example:
power([1,2,3])
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
'''

def power(s):
   	"""Computes all of the sublists of s"""
   	length = len(s)
   	count = 2**length 
   	result = []
   	for i in range(count):
   		st = str(bin(i)[2:]).zfill(length)
   		temp = []
   		for j in range(length):
   			if st[length - 1 - j] == str(1):
   				temp.append(s[j])
   		result.append(temp)
   	return result

def powersetlist(s):
    r = [[]]
    for e in s:
       # print "r: %-55r e: %r" % (r,e)
        r += [x+[e] for x in r]
    return r
 
s= [0,1,2,3]    
#print "\npowersetlist(%r) =\n  %r" % (s, powersetlist(s))


#print power([0,1,2,3])
   
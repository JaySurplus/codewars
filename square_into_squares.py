"""
	Square into Squares. Protect trees!
	http://www.codewars.com/kata/square-into-squares-protect-trees
"""
import math

def decompose(n):
    # your code
    def sub_decompose(s,i):
    	if s < 0 :
    		return None
    	if s == 0:
    		return []
    	for j in xrange(i-1, 0 ,-1):
    		#print  s,s - j**2 ,j
    		sub = sub_decompose(s - j**2, j)
    		#print j,sub
    		if sub != None:
    		#	print  s,j,sub
    			return sub + [j]
    return sub_decompose(n**2,n)

if __name__ == "__main__":
	print decompose(11)

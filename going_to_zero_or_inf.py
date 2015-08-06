"""
Going to zero or to infinity?
http://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python
"""

import math
def going(n):
	'''	
	def inter(n):
		if n == 1: 
			return 1
		else:
			return 1 + 1.0 * (n-1) / n
	'''
	 
	result = 0
	for i in range(n):
		result = 1.0*result/(i+1) + 1
	return math.floor(result * (10**6))/(10**6)




if __name__ == "__main__":
	for i in range(10):
		print i, going(i)
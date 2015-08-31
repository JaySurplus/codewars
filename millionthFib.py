"""
	The Millionth Fibonacci Kata
	http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""
import math
import sys
from collections import defaultdict

def fib(n):

	dic = defaultdict(list)

	def find_dim(k):
		if k == 0:
			return []
  		if k == 1:
  			return [0]
  		else:
  			return [int(math.log(k,2))] + find_dim(k - 2**(int(math.log(k,2))))
	  		
	def matrix_multi(a, b):
		return [a[0]*b[0]+a[1]*b[2],
				a[0]*b[1]+a[1]*b[3],
				a[2]*b[0]+a[3]*b[2],
				a[2]*b[1]+a[3]*b[3]]

  	
	def matrix_power(pow):
		a = [1,1,1,0]
		if pow in dic:
			return dic[pow]
		else:
			if pow == 0:
				return a
			else:
				for i in range(1,pow+1):
					if i not in dic:
						a = matrix_multi(a , a)
						dic[i] = a
						
					else:
						a = dic[i]
 				return a
	#print matrix_power([1,1,1,0])

	def get_fib(t):
		if t == 0 or t == 1:
			return t
		else:
			result = [1,0,0,1]
			alist = find_dim(t-1)
			for i in alist:
				result = matrix_multi(result,matrix_power(i))
			return result[0]
	


	return get_fib(n) if n >= 0 else (-1)**(n%2+1) *get_fib(-n)

def main():
	try:
		var = int(raw_input("Please enater a number:"))

		result = fib(var)
		print "The %dth fib number is %d"%(var , result)
	except:
		pass
	

if __name__ == '__main__':
	main()



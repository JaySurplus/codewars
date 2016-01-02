"""
	The Millionth Fibonacci Kata
	http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""
import math
import sys
import time
from collections import defaultdict

# following not working , took too much time to compute.

def fib(n , i):


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

	def matrix_fib(t):
		if t == 0 or t == 1:
			return t
		else:
			result = [1,0,0,1]
			alist = find_dim(t-1)
			for i in alist:
				result = matrix_multi(result,matrix_power(i))
			return result
	
	def dynamic_fib(n):
		a = 0
		b = 1
		if n == 0:
			return (a , b)
	
		for i in range(n):
			temp = a + b
			a = b
			b = temp
		return (a , b )



	def double_fast(n):
		#really fast
		if n == 0:
			return (0 , 1)
		else:
			a, b = double_fast(n/2)
			c = a * (2* b -a )
			d = b **2 + a**2
			if n%2 == 0:
				return (c , d)
			else:
				return (d , d+c)

	def compute_fib(n ,i ):
		func = {0: matrix_fib,
		        1: double_fast,
		        2: dynamic_fib }


		return func[i](n)[0] if n >= 0 else (-1)**(n%2+1) * func[i](-n)[0]




	
	return compute_fib(n , i)

def size_base10(n):
		size = 0
		while n /10 != 0:
			size += 1
			n = n/10
		
		return size


def main():
	'''
		func = {0: matrix_fib,
		        1: double_fast,
		        2: dynamic_fib }
	'''
	try:
		#var = int(raw_input("Please enter the n-th Fib number you want:"))
		var = 200000
		start = time.time()
		i = 1
		result = fib(var , i)

		end = time.time()
		
		#print "Lenght of %dth fib number is %d" %(var , size_base10(result))
		print "Time is %s seconds." % (end - start)
		#print "The %dth fib number is %d"%(var , result)
	except:
		pass
	

if __name__ == '__main__':
	main()




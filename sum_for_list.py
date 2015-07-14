#!/usr/bin/python
from collections import defaultdict

def sum_for_list(lst):
	
	
	aDict = defaultdict(lambda : 0)
	
	
	def primes(n):

		d = 2
		aN = n
		n = abs(n)
		while d*d <= n:
			aBool = True
			while (n % d) == 0:
				#primfac.add(d)   # supposing you want multiple factors repeated
				if aBool:
					aDict[d] += aN
					aBool = False
				n /= d
			d += 1
		if n > 1:
			aDict[n] += aN	
		return aDict
	for i in lst:
		primes(i)
		#primes(i)

	
	result = [ [k,v] for k,v in aDict.iteritems()]
	result.sort(key = lambda x:x[0])
	return result

a = [12,15]
b =  [15, 30, -45] 
c = [15, 21, 24, 30, 45]
test = sum_for_list(b)


#print test
#print sum_for_list(a)
d = sum_for_list(c)
print d
d.sort(key = lambda x: x[0] ,reverse =True)
print d
 
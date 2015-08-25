"""
	Decimal to any Rational or Irrational Base Converter	
	http://www.codewars.com/kata/5509609d1dbf20a324000714/train/python

	wiki_page : https://en.wikipedia.org/wiki/Non-integer_representation

"""
import math
from math import pi , log
'''
def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    #your code here
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m = 1
    if n < 0:
        n = -n
        m = -m
   
    times = 0 if n == 0 else int(math.floor(math.log(n, base))) 
    
    result = ''

    while times >= -decimals :
        if times == -1:
            result += '.'
        val = int(n / base**times)

        result+=alpha[val]
        #print "base time " ,n/(base**times)
        n -= int(n / base**times) * base**times
       
        #print result,n , times
       
        times-=1
    if m == -1:
        result = '-'+result
    result = str(result)
    if decimals != 0:
        loc = result.index('.')
        last = len(result)-1
        if decimals > last - loc:
            result+='0'* (decimals-(last - loc))
    return result
    
'''


def converter(n , decimals = 0 , base = pi):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0 : return '0' if not decimals else '0.' + '0'*decimals

    result = '' if n > 0 else '-'

    n = abs(n)

    for i in range(int(log(n, base)) , -decimals -1, -1 ):
        if i == -1: 
            result += '.'
        result +=  alpha[int(n / base**i)]
        n %= base**i
    return result

def main():
    print converter(0,4,26)
    print converter(-15.5,2,23)
    print converter(13,0,10)
    print converter(5.5, 1,10)
if __name__ == '__main__':
	main()
    

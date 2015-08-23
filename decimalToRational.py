"""
	Decimal to any Rational or Irrational Base Converter	
	http://www.codewars.com/kata/5509609d1dbf20a324000714/train/python

	wiki_page : https://en.wikipedia.org/wiki/Non-integer_representation

"""

from math import pi

def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    #your code here
    alphabeta = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
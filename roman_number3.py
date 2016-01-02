ø"""
	Roman Numerals Helper
	http://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
"""
import re

class RomanNumberHelper:

	def __init__(self):

		self.alist = [(1000,'M'), (900,'CM') , (500,'D') , (400 , 'CD'),
			(100,'C'),(90,'XC'), (50,'L'), (40, 'XL') , (10,'X'),
			(9,'IX'), (5,'V'),(4,'IV'),(1,'I')]



	def to_roman(self, number):
		result = ''
		for (num, letter) in self.alist:
			result+= (number/num)*letter
			number = number%num
		return result

	def from_roman(self, roman):
		result = 0
		i = 0
		while i < len(self.alist):
			reg = '^'+self.alist[i][1]
			if re.search(reg , roman) != None:
				result += self.alist[i][0]
				roman = re.sub(reg,'',roman)
				
			else:
				i+=1
		return result

if __name__ == "__main__":
	romanNumberals = RomanNumberHelper()
	print "Number: %s"%romanNumberals.to_roman(1666)
	print romanNumberals.from_roman('MDCLXVI')
	print romanNumberals.from_roman('XXI')
	print romanNumberals.from_roman('IV')
"""
	Roman Numerals Helper
	http://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
"""


class RomanNumberHelper:

	result = ""

	def to_roman(self, number):
		self.result = str(number)
		return self.result

	def from_roman(self, roman):
		self.result = roman
		return self.result


if __name__ == "__main__":
	romanNumberals = RomanNumberHelper()
	print romanNumberals.to_roman(5)
	print romanNumberals.from_roman('M')
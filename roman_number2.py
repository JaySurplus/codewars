def solution(n):
# TODO convert int to roman string
	result = ""
	roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }

	
	for key in sorted(roman_numerals.keys() , reverse = True ):
		while n >= key:
			result += roman_numerals[key]
			n -= key
#			print key , n,roman_numerals[key]
	return result

print solution(999)
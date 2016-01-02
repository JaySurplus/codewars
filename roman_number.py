def solution(n):
# TODO convert int to roman string
	result = ""
	

	remainder = n
	if n == 0:
		return ""
	for i in range(0,len(roman_number)):
		time = 1.0*remainder/roman_number[i][0]
		if str(roman_number[i][0])[0] == '1':
			if time < 4 and time >=1:
				temp = remainder % roman_number[i][0]
				div = remainder / roman_number[i][0]
				remainder = temp
				result += div * roman_number[i][1]
			if time < 1 and time >= 0.9:
				result += (roman_number[i+2][1]+roman_number[i][1])
				remainder = remainder % roman_number[i+2][0]
		else:
			if  time < 1 and time >= 0.8:
				result += (roman_number[i+1][1]+roman_number[i][1])
			   	remainder = remainder % roman_number[i+1][0]
			if time >= 1 and time < 1.8:
				div = (remainder - roman_number[i][0]) / roman_number[i+1][0]
				result += roman_number[i][1] + div * roman_number[i+1][1]
				remainder = remainder % roman_number[i+1][0]
			if time >= 1.8:
				result +=  roman_number[i+1][1]+roman_number[i-1][1] 
				remainder = remainder % roman_number[i+1][0]
	return result
			
roman_number = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]

#print solution(4)
#print solution(6)
print solution(3991)
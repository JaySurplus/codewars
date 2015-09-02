"""
	Vigenere Autokey Cipher Helper
	http://www.codewars.com/kata/vigenere-autokey-cipher-helper
"""

class VigenereAutokeyCipher:
	def __init__(self, key, alphabet):
		self.key = key
		self.alphabet = alphabet
		
	def code(self, text, direction):

		toText = list(text)
		result = []
		newKey = filter(lambda x: (x in self.alphabet) == True, list(self.key)) #+  filter(lambda x: (x in self.alphabet) == True, toEncode)
	
		#print  'new' ,newKey	
		j = 0	
		for i in range(len(toText)):
			#print i ,self.key[i%(len(self.key))]
			if toText[i] in self.alphabet:
				if direction:
					newKey.append(toText[i])
					result.append(self.alphabet[(self.alphabet.index(toText[i]) + self.alphabet.index(newKey[j]))%len(self.alphabet)])
				else:
					result.append(self.alphabet[(self.alphabet.index(toText[i]) - self.alphabet.index(newKey[j]))%len(self.alphabet)])
					newKey.append(result[-1])
				j += 1
			else:
				result.append(toText[i])
		return ''.join(result)


	def encode(self, toEncode):
		return self.code(toEncode,1)
		


	def decode(self, toDecode):
		return self.code(toDecode, 0)


def main():
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	#alphabet = 'abcdefgh'
	key = 'password'
	tester = VigenereAutokeyCipher(key,alphabet)

	print tester.encode('codewars')
	print tester.encode('amazingly few discotheques provide jukeboxes') 
	print 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'

	print tester.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')
	print 'amazingly few discotheques provide jukeboxes'

if __name__ == '__main__':
	main()
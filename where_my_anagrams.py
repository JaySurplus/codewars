'''
	Where my anagrams at?
	http://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
	Also could construct prime list, assign each character from word to a prime number. multiply them 
	then divid prime number from word in words.
'''

def anagrams(word, words):
    #your code here
    
    return filter(lambda x: sorted(x) == sorted(word) , words)
  


print anagrams("thisis" , ["thisis", "isthis", "thisisis"])
print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print anagrams('laser', ['lazing', 'lazy',  'lacer'])
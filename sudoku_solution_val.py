"""
	Sudoku Solution Validator
	http://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
"""

def validSolution(board):
	test = range(1,10,1)
	def tester(alist):
		return set(test)==set(alist)

	for i in range(len(board)):
		tem = board[i]
		if not tester(tem):
			return False
	
	
	for i in range(len(board[0])):
		if not tester([alist[i] for alist in board]):
			return False


	for i in range(3):
		for j in range(3):
			if not tester(sum([alist[j*3:j*3+3] for alist in board[i*3:i*3+3]] , [])):
				return False

	return True


boardOne = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
               [6, 7, 2, 1, 9, 0, 3, 4, 8],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]]


boardTwo =[[5, 3, 4, 6, 7, 8, 9, 1, 2], 
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]


print validSolution(boardOne)
print validSolution(boardTwo)
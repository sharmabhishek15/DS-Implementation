from typing import *


def toeplitzMatrix(n: int, m: int, mat: List[List[int]]) -> bool:
	# Write your code here.
	i = 0
	first = 0
	result = ''
	if m == 0 or n == 0 or m != n:
		result = 'NO'
		return result

	for lt in mat:
		val = lt[i]
		if i == 0:
			i = i + 1
			first = val
			continue
		else:
			i = i + 1
			if first != val:
				result = 'NO'
				return result
	result = 'YES'
	return result

m = 3 # colmun
n = 4 # row
#mat = [[10, 10, 10],[4, 10, 10],[2, 10, 10], [4,  4, 8]]
mat = [[0, 0, 0],[7, 0, 1],[1, 7, 0], [0,  1, 7]]
#mat = [[2, 1, 3],[1, 2, 1],[5, 1, 2]]
print(toeplitzMatrix(n, m, mat))
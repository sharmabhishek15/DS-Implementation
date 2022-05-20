from typing import *


def toeplitzMatrix(n: int, m: int, mat: List[List[int]]) -> bool:

	"""
		Problem Statement
		You are given a matrix of size N * M. You have to find out whether the matrix is Toeplitz or not.
		A Matrix is said to be Toeplitz if every diagonal from top-left to bottom-right has the same elements.
		You are given the matrix ‘MAT’ of size N * M.Your task is to find out whether it is Toeplitz or not.
		For Example
		 The given matrix is Toeplitz:

		Input Format:
		The first line of the input contains an integer, 'T,’ denoting the number of test cases.

		The first line of each test case contains two integers,' N’ and ‘M’ denoting the number of rows and columns.

		The next line of each test case has ‘N’ lines that have M values corresponding to the matrix ‘MAT’.
		Output Format:
		For each test case, print ‘YES’ or ‘NO’ whether the matrix is Toeplitz or not.

		 Print the output of each test case in a separate line.
		Note:
		You do not need to print anything. It has already been taken care of. Just implement the given function.
		Constraints:
		1 <= T <= 10
		1 <= N <= 1000.
		1 <= M <= 1000.

		Time limit: 1 sec
		Sample Input 1:
		2
		3 3
		2 1 3
		1 2 1
		5 1 2
		4 3
		0 0 0
		7 0 1
		1 7 0
		0 1 7
		Sample Output 1:
		YES
		NO
	"""
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
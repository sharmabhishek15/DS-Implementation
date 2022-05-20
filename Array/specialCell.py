def checkUnique(mat, n, m, i, j):
    countRow = 0
    for k in range(m):
        countRow += mat[i][k]
        if countRow > 1:
            return False

    countCol = 0
    for k in range(n):
        countCol += mat[k][j]
        if countCol > 1:
            return False

    return True


def specialCellInBinaryMatrix(n: int, m: int, mat: List[List[int]]) -> int:
    """
        Problem Statement
        Ninja is observing a Binary matrix of size N * M . A Binary Matrix is made up of only 0’s and 1’s. Ninja wants to know the number of special cells in the matrix. The conditions of a cell to be a special cell are:
        The value of M[i][j] should be 1.
        All other cells of row i should be 0.
        All other cells of column j should be 0.
        You are given the matrix ‘MAT’ of size N * M. Your task is to find the number of special cells in the given matrix.
        For Example
        For the matrix :
          1  0  0
          0  0  0
          0  1  0

        The Answer will be 2 as cell (0,0) and (2,1) are special.(Indexing is 0 based).
        Input Format:
        The first line of the input contains an integer, 'T,’ denoting the number of test cases.

        The first line of each test case contains two integers,' N’ and ‘M’ denoting the number of rows and columns.

        The next line of each test case has ‘N’ lines that have M values corresponding to the matrix ‘MAT’.
        Output Format:
        For each test case, print an integer corresponding to the number of special cells in the matrix.

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
        1 0 0
        0 0 0
        0 1 0
        4 3
        1 0 0
        0 0 1
        0 0 0
        0 1 1
        Sample Output 1:
        2
        1
    """
    # Write your code here.
    countUnique = 0
    for i in range(n):
        for j in range(m):
            if (mat[i][j] and checkUnique(mat, n, m, i, j)):
                countUnique += 1

    return countUnique
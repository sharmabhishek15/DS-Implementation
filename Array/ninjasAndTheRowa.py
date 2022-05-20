from typing import *


def maximumWeightRow(n: int, m: int, mat: List[List[int]]) -> int:
    """
        Problem Statement
        Ninja has been provided a matrix 'MAT' of size 'N X M' where 'M' is the number of columns in the matrix, and 'N' is the number of rows.
        The weight of the particular row is the sum of all elements in it. Ninja wants to find the maximum weight amongst all the rows.
        Your task is to help the ninja find the maximum weight amongst all the rows.
        EXAMPLE:
        Input: 'N' = 2, 'M' = 3, 'MAT' = [[1, 2, 3], [2, 0, 0]]
        Output: 6
        
        The weight of first row is 1 + 2 + 3 = 6
        The weight of the second row is 2 + 0 + 0 = 2; hence the answer will be a maximum of 2 and 6, which is 6.
        Input Format :
        The first line of input contains an integer 'T', denoting the number of test cases. 
        
        For each test case, the first line will contain two integers, 'N' and 'M' number of rows and columns in the matrix. Next, 'N' lines will contain 'M' integers for each of the matrix elements.
        Output Format :
        For each test case, print the maximum weight amongst all the rows.
        Note :
        You don't need to print anything. It has already been taken care of. Just implement the given function.
        Constraints :
        1 <= 'T' <= 10
        1 <= 'N' <= 10^2
        1 <= 'M' <= 10^2
        0 <= 'MAT[I][J]' <= 10^5
        
        Time Limit: 1 sec
        Sample Input 1 :
        2
        3 3
        1 2 3
        3 4 2
        3 4 2
        1 1
        2
        Sample Output 1 :
        9
        2
    """


    # Write your code here.
    maxw = 0
    for i in mat:
        m = sum(i)
        maxw = max(m, maxw)

    return maxw
def maximumPoints(n: int, grid):
    """
        Problem Statement
        You are playing a video game, which contains an N x N grid. You start on the top left cell of the grid, and are free to move anywhere through the grid, any number of times.
        Each cell in the grid has some number of points that you can collect from it and you can collect points at most once from each cell. Furthermore, it is possible to collect points from a cell, if and only if the cell lies on one of the two diagonals of the grid. Print the maximum number of points you can collect, given the grid.
        For example:
        If the grid is:
        1 2
        3 4
        We can collect points from all cells as each cell lies on a diagonal. So, the maximum points will be 1+2+3+4 = 10.
        Input Format:
        The first line contains 'T', denoting the number of test cases.
        For each Test :
        The first line contains an integer ‘N’.
        The next ‘N’ lines contain ‘N’ space separated integers each, representing the grid.
        Output Format:
        Print one integer, the maximum number of points you can gain from the grid.
        Note:
        You are not required to print the expected output. It has already been taken care of. Just implement the function.
        Constraints -
        1 <= 'T' <= 10
        1 <= ‘N’ <= 1000.
        1 <= ‘A[i][j]’ <= 1000, i ∈ [1,N], j ∈ [1,N]
        Note: It is guaranteed that the sum of N^2 across all test cases will be at most 10^6.
        Time Limit: 1 sec
        Sample Input 1:
        2
        3
        1 2 3
        4 5 6
        7 8 9
        1
        5
        Sample Output 1
        25
        5
    """
    # Write your code here.
    total = 0
    if n == 0:
        return total
    if n > 2:
        itr = 0
        n = n-1
        while n >= 0:
            #print("itr, n", itr, n)
            #print(grid[itr][itr])
            if itr == n:
                total += grid[itr][itr]
            else:
                total += grid[itr][itr]
                total += grid[itr][n]
            itr += 1
            n -= 1
            #print("total", total)
    else:
        for itr in grid:
            total += sum(itr)
    return total

matrx = [
            [0, 1, 2],
            [5, 6, 7],
            [2, 1, 2]
        ]
n = 3
print(maximumPoints(n,grid=matrx))
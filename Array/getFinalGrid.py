def getFinalGrid(a, n):
    """
        Problem Statement
        Luke, a naughty kid, went to a museum one day. He sees an ancient grid 'A' consisting of 'N' rows and 'N' columns. Each cell of a grid is coloured with either black or white.
        Luke performs two sequential operations on the grid ‘A’. First, he twists the grid vertically around the center. After that, as the second operation, he changes the colours of all the cells. If the cell is white, it is changed to black and vice-versa.
        Sample Input 1 :
        2
        3
        1 1 0
        0 1 1
        1 0 0
        1
        0
        Sample Output 1 :
        1 0 0
        0 0 1
        1 1 0
        1

    """
    # Write your code here.
    temp = a.copy()
    rowCounter = 0
    for row in temp:
        s = 0
        e = n - 1
        # print(row)
        while s <= e:
            if s==e:
                # print(a[rowCounter][s])
                midValue = 1 if row[s] == 0 else 0
                a[rowCounter][s] = midValue
                # print(a)
            else:
                # print("before ",a[rowCounter][s], a[rowCounter][e])
                value1 = 1 if row[s] == 0 else 0
                value2 = 1 if row[e] == 0 else 0

                a[rowCounter][s], a[rowCounter][e] = value2, value1
                # print("after ",a[rowCounter][s], a[rowCounter][e])
                # print(a)
            s += 1
            e -= 1
        rowCounter += 1
    return a

grid = [
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 0]
        ]
length = 3
print(getFinalGrid(grid, length))
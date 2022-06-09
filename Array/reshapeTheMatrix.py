def arrange(n: int, m: int, b, r: int, c: int):
    """
        Problem Statement
        One of your friends started working at a toy store, and today is his first day. He gets a box of some toys. The box looks like a grid 'B' consisting of 'N' rows and 'M' columns, and each cell has exactly one toy. His task is to arrange these toys on the shelf 'S' in front of him, which is empty. The shelf has 'R' rows and 'C' columns. Help your friend to arrange the toys on the shelf 'S' in the same row-order traversal as in the box 'B'.
        You are given the box arrangement of toys in a matrix of size 'N * M' where values in the matrix are integers and denote the IDs of toys. Your task is to return a matrix of size 'R * C' denoting the shelf arrangement of toys.
        After arranging the toys on the shelf 'S', if any toy remains in the box or any cell remains empty in the shelf, return the given box arrangement.
        Sample Input 1 :
        2
        2 4
        5 0 3 2
        1 5 5 3
        4 2
        3 3
        3 2 6
        1 2 3
        5 1 9
        2 4
        Sample Output 1 :
        5 0
        3 2
        1 5
        5 3
        3 2 6
        1 2 3
        5 1 9
    """
    # Write your code here.
    result = []
    itr = 0
    start = 0
    end = c

    if n * m == r * c:
        temp = []
        for lt in b:
            temp.extend(lt)

        while itr < r:
            result.append(temp[start:end])
            start = end
            end = end + c
            itr += 1
        return result
    else:
        return b


n = 2
m = 4
r = 4
c = 2
b = [
    [5, 2, 4, 7],
    [6, 3, 4, 2]
]
print(arrange(n, m, b, r, c))

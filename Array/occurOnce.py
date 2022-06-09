def occursOnce(a, n):
    """
        Problem Statement
        You are given an array A of length N, where N is always an odd integer. There are (N-1)/2 elements in the array that occur twice and one element which occurs once. Your task is to find the only element that occurs once in the array.
        Note: There are (N-1)/2+1 elements that are unique in the array.
        Sample Input 1:
        2
        7
        7 3 5 4 5 3 4
        9
        5 6 9 6 1 9 1 5 3
        Sample Output 1:
        7
        3
    """
    # Write your code here.
    temp = {}

    for i in a:
        if i in temp:
            del temp[i]
        else:
            temp[i] = 1
    return next(iter(temp))
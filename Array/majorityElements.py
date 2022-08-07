from math import *

def findMajorityElement(arr, n):
    # Write your code here.
    dict = {}
    for item in arr:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1

    for key, value in dict.items():
        if floor(n / 2) <= value:
            return key
    return -1


arr = [5, 2, 0, 0 ]
n = 4
print(findMajorityElement(arr, n))
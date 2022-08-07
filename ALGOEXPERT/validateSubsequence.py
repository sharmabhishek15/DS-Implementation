
'''

  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers
   = [5, 1, 22, 25, 6, -1, 8, 10]
    = [1, 6, -1, 10]
'''
def isValidSubsequence(array, sequence):
    # Write your code here.
    arrayPointer = 0
    seqPointer = 0

    while arrayPointer < len(array) and seqPointer < len(sequence):
        if array[arrayPointer] == sequence[seqPointer]:
            seqPointer += 1
        arrayPointer += 1

    return seqPointer == len(sequence)
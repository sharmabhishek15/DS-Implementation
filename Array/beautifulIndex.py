def beautifulIndex(N, A) -> int:
    # Write your code here.
    start = 0
    end = N - 1

    while start <= end:
        print(start - 1, end - start)
        if start - 1 == end - start:
            return start
        start += 1
    return -1

A = [1, 1, 1]
N = 3
print(beautifulIndex(N, A))
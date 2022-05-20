
def higherlower(n):
    global guesser
    if guesser == n:
        return 0
    elif guesser > n:
        return -1
    else:
        return 1

def numberGuess(n: int, guesser) -> int:
    # Write your code here.
    lt = list(range(0, n + 1))
    start = 0
    end = lt[-1]
    mid = start + ((end - start) // 2)
    while mid >= start or mid <= end:
        mid = start + ((end - start) // 2)
        temp = higherlower(mid)
        if temp == 0:
            return mid
        elif temp == -1:
            start = mid + 1
        else:
            end = mid - 1
    return 0
n = 10
guesser = 10
print(numberGuess(n,guesser))
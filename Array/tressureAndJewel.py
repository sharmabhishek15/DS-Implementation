def treasureAndJewels(n: int, m: int, stones: str, jewels: str) -> int:
    """
        Problem Statement
        Ninja luckily found a treasure hidden in his backyard. He found some stones in the treasure box and Ninja thought that these stones could be valuable. He went to a stone expert, and the expert gave him a list ‘JEWELS’ consisting of the names of all valuable jewels. Ninja made the list ‘STONES’ of all stones he found in the treasure. All stones and Jewels are represented by English characters. Now, Ninja wants to know the number of jewels he found in the treasure box. Can you help the Ninja?
        Note: ‘JEWELS’ consist of distinct characters and ‘A’ and ‘a’ are treated as two different stone types.
        For Example
        If ‘STONES’ is “abAAc” and JEWELS is “Acd”.The number of jewels Ninja have is 3.
        Input Format:
        The first line of the input contains an integer, 'T,’ denoting the number of test cases.

        The first line of each test case contains two integers, ‘N’ denoting the number of stones and M denoting the number of Jewels.

        The second line of each test case contains an string of size N denoting ‘STONES’

        The third line of each test case contains an string of size M denoting ‘JEWELS’
        Output Format:
        For each test case, print an single integer denoting the number of jewels Ninja found in the treasure box.

        Print the output of each test case in a separate line.
        Note:
        You do not need to print anything. It has already been taken care of. Just implement the given function.
        Constraints:
        1 <= T <= 10
        1 <= N <= 10000.
        1 <= M <= 52

        Time Limit = 1 sec
        Sample Input 1:
        2
        5 3
        abAAc
        Acd
        4 2
        acbd
        Aa
        Sample Output 1:
        3
        1
    """
    # Write your code here.
    res = 0
    jewDict = {}
    for jewl in jewels:
        if not jewDict.get(jewl):
            jewDict[jewl] = 1

    for stone in stones:
        if jewDict.get(stone):
            res += 1

    return res
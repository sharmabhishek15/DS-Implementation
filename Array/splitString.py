def splitString(string: str) -> bool:
    # Write your code here.
    """
        You are given a string ‘str’ of even length. Your task is to find out if we divide the ‘str’ from the middle, will both the substrings contain an equal number of vowels or not.
        For Example:
        You are given, ‘str’= ‘codingninjas’, when we split this string we get, ‘coding’ and ‘ninjas’ which both contain 2 vowels each. Hence the answer is ‘True’.
        Input Format:
        The first line of input contains a single integer ‘T’, representing the number of test cases.

        The first line of each test case contains a string ‘str’ representing the given string.
        Output Format:
        For each test case, print a "True” or “False" depending on if the halves of the string have an equal number of vowels or not.

        Print a separate line for each test case.
        Sample Input 1:
            2
            codingninjas
            helloworld
        Sample Output 1:
            True
            False
    """
    temp = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True,
        'A': True,
        'E': True,
        'I': True,
        'O': True,
        'U': True,
    }
    if len(string) % 2 != 0:
        return False
    else:
        mid = len(string) // 2
        firstHalf = string[:mid]
        secondHalf = string[mid:]
        countFirst = 0
        countSecond = 0

        for ch in firstHalf:
            if temp.get(ch):
                countFirst += 1

        for ch in secondHalf:
            if temp.get(ch):
                countSecond += 1

        if countFirst == countSecond:
            return True
        else:
            return False



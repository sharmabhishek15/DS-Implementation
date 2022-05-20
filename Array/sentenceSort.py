def sentenceSorting(string: str) -> str:
    """
        Problem Statement
        You are given a sentence in the form of a string ‘str’ containing no more than 9 words, each word in the sentence is suffixed by a unique number ranging from 1 to N, where N is the number of words in the sentence. Your task is to reorder the words in ‘str’ according to the suffix number of each word and return it as the string.
        For Example:
        You are given ‘str’ = ‘A1 person3 good2’, in this we can see the ordering of the words like ‘A’,  ‘good’ ‘person’ according to the suffix number. Hence the answer string is ‘A good person’.
        Input Format:
        The first line of input contains a single integer ‘T’, representing the number of test cases.

        The first line of each test case contains a string ‘str’ representing the given string.
        Output Format:
        For each test case, print a single string representing the sorted string.

        Print a separate line for each test case.
        Constraints:
        1 <= T <=  10
        1 <= |str| <= 10^6

        ‘str’ will contain upper and lower case characters of the English alphabet.
        ‘str’ will not contain more than 9 words.

        Time Limit: 1 sec.
        Note :
        You do not need to print anything. It has already been taken care of. Just implement the given function.
        Sample Input 1:
        2
        A1 person3 good2
        world2 hello1
        Sample Input 2:
        A good person
        hello world

    """

    # Write your code here.
    temp = {}
    ans = ''
    for sen in string.split():
        if not temp.get(sen):
            temp[sen[-1]] = sen[:-1]

    for i in range(1, len(string.split()) + 1):
        ans += temp[str(i)] + ' '

    return ans
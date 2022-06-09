from collections import deque
import time

def minimize_the_string(str):
	"""
		Input: S = “aabcccabba”
		Output1: 4
		Output2 = "ccca"
		Explanation:
		Divide the given string S in two parts as “aabcc” and “cabba”. Below are the operations performed on the above two substrings:

		Remove the prefixes and suffixes of the same characters, i.e. ‘a’. The string becomes “bcc” and “cabb”.
		Remove the suffixes and prefixes of the same characters, i.e. ‘b’. The string becomes “cc” and “ca”.
		Now, after concatenating the right and left substrings, the string obtained is “cacc”, which is of the shortest length, i.e. 4.

		Input: S = “aacbcca”
		Output1: 1
		Output2 =
	"""
	i = 0
	j = len(str) - 1
	stack = deque()
	result = ""

	while i <= j:
		target = str[i]
		if str[i] == str[j] and i != j:
			while i < j and str[i] == target:
				stack.append(str[i])
				i += 1

			while i < j and str[j] == target:
				stack.append(str[j])
				j -= 1
			while stack:
				if target == stack[-1]:
					stack.pop()
		else:
			i += 1
			stack.append(target)

	while stack.__len__() > 0:
		result += stack.pop()
	return result[::-1]

start_time = time.time()
# print("Start of function - ", start_time)

st = "aabcccabba"
print(minimize_the_string(st))

end_time = time.time() - start_time
print("End of function - ", end_time)



def minimize_the_string2(str):
    """
        "aabcccabba"
        break string in two parts l and r
        l = "aabcc"
        r = "cabba"
        str = r + l
        str = "cabbaaabcc"
        if suffix of r matches with refix of l
        eg a at index 4 and a at index 5, remove:
        str = "cabbbcc" and so on.
    """
    mid = len(str)//2
    l = str[:mid]
    r = str[mid:]
    str = r+l
    i = mid -1
    j = mid
    stack = deque()
    result = ""

    while i != 0 or j < len(str):
        target = str[i]
        if str[i] == str[j]:
            while i != 0 and str[i] == target:
                stack.append(str[i])
                i -= 1

            while i != 0 and str[j] == target:
                stack.append(str[j])
                j += 1
            while stack:
                if target == stack[-1]:
                    stack.pop()
        else:
            if i != 0:
                i -= 1
            else:
                j += 1
            stack.append(target)

    while stack.__len__() > 0:
        result += stack.pop()
    return result[::-1]


start_time = time.time()
# print("Start of function - ", start_time)

st = "aabcccabba"
print(minimize_the_string2(st))

end_time = time.time() - start_time
print("End of function - ", end_time)
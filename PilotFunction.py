# function to remove adjacent duplicate characters in the string.
# input = 'aaddnndellk'
# output = 'dek'
from collections import deque

str = 'aaddnndellk'
# stack = deque()
stack = []
last_char = ''
count = 0
for index,char in enumerate(str):

    if index:
        if last_char == char:
            stack.append(char)
            count += 1
        else:
            if count > 0:
                while count != 0:
                    stack.pop()
                    count -= 1
                stack.pop()
            stack.append(char)
    else:
        stack.append(char)

    last_char = char
print(stack)

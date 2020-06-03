#Program to convert normal expression in postfix expression, using stack.


class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.head = None



	def is_empty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self,new_data):
		if self.head == None:
			self.head = Node(new_data)
		else:
			new_node = Node(new_data)
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.is_empty():
			return None
		else:
			popNode = self.head
			self.head = popNode.next
			popNode.next = None
			return popNode.data

	def top(self):
		if self.is_empty():
			return None
		else:
			return self.head.data


def checkForOperand(char):
	return True if char.isalpha() else False


def checkForPrecedence(topOfStack, i):
	precedenceDict = { '+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3 }
	return True if precedenceDict[topOfStack] > precedenceDict[i] else False


def conversionInfixtoPostfix(stack,str):
	newStr = ''
	for i in str:
		if i == '(':
			stack.push(i)
		elif checkForOperand(i):
			newStr = newStr + i
		elif i == ')':
			while (not stack.is_empty() and stack.top() != '(' ):
				newStr += stack.pop()
			if 	not stack.is_empty() and stack.top() != '(':
				return -1
			else:	
				stack.pop()
		else:
			while (not stack.is_empty() and stack.top() != '(' and checkForPrecedence(stack.top(),i) ):
				newStr += stack.pop()
			stack.push(i)
	while not stack.is_empty():
		newStr += stack.pop()
	
	return newStr


def reverseString(expression):
	return expression[::-1]


def reverseBraces(expression):
	a = ''
	expression = list(expression)
	for i in expression:
		if i == ')':
			a += '('
		elif i == '(':
			a += ')' 
		elif i == " "
			pass
		else:
			a += i
	return a

str = "((A+B)*C-D)*E"
str = reverseString(str)
newStr = reverseBraces(str)
stackObj = Stack()
output = conversionInfixtoPostfix(stackObj,newStr)
result = reverseString(output)
print(result)
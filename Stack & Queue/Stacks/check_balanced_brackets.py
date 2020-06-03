#check for balanced paranthesis, curly braces, square braces.
# like [{} () ()] 
# not like  [{}()(]) it should be in order of latest opening of bracket should close first of similar type.



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


def balaceTheParanthesis(stack,str):
	for i in str:
		if i == '[' or  i == '{' or i == '(':
			stack.push(i)
		if stack.is_empty():
			return False
		if i == ']':
			item = stack.pop()
			if item == '(' or item == '{':
				return False
		elif i == '}':
			item = stack.pop()
			if item == '[' or item == '(':
				return False
		elif i == ')':
			item = stack.pop()
			if item == '{' or item == '[':
				return False
		else:
			pass

	if stack.is_empty():
		return True		

str = "[{()}]"
stackObj = Stack() 

result = balaceTheParanthesis(stackObj,str)
if result:
	print("Balanced")
else:
	print("Not Balanced")

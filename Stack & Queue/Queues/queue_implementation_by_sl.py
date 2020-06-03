class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None


	def enqueue(self,new_data):
		if self.head == None:
			new_node = Node(new_data)
			self.head = new_node
			self.tail = self.head
		else:
			new_node = Node(new_data)
			self.tail.next = new_node
			self.tail = new_node



	def dequeue(self):
		if self.is_empty():
			return "Queue is Empty."
		first_node = self.head
		self.head = first_node.next
		first_node = None
		 


	def lastNode(self):
		if self.head == None:
			return "Empty Queue"
		return self.tail.data


	def top(self):
		if not self.is_empty():
			return self.head.data


	def is_empty(self):
		return True if self.head == None else False 

queueObj = Queue()
queueObj.enqueue(5)
queueObj.enqueue(4)
queueObj.enqueue(3)
print("Last value of Queue " , queueObj.lastNode())
queueObj.dequeue()

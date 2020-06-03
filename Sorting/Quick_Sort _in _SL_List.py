# Python 3 program to find the number 
# of nodes in looop in a linked list  
# if loop is present 
  
# Python Code to detect a loop and  
# find the length of the loop 
# Node defining class 
class Node: 
	  
	# Function to make a node 
	def __init__(self, val): 
		self.data = val 
		self.next = None
	  
# Linked List defining and loop  
# length finding class  
class LinkedList: 
	  
	# Function to initialize the  
	# head of the linked list 
	def __init__(self): 
		self.head = None        
		  
	# Function to insert a new  
	# node at the end  
	def AddNode(self, val): 
		if self.head is None: 
			self.head = Node(val) 
		else: 
			curr = self.head 
			while(curr.next): 
				curr = curr.next
			curr.next = Node(val) 
	  
	def partition(self,start,end):
		pivot_prev = start
		curr = start
		pivot = end
		while (start != end):
			if start.data < pivot.data:
				pivot_prev = curr  
				temp = curr.data  
				curr.data = start.data 
				start.data = temp
				curr = curr.next 
			start = start.next
		temp = curr.data  
		curr.data = pivot.data    
		return pivot_prev 
	  
	def sort(self,start,end):

		if start == end:
			return start
		pivot_prev = self.partition(start,end)
		self.sort(start,pivot_prev)
		# // if pivot is picked and moved to the start, 
		# // that means start and pivot is same  
		# // so pick from next of pivot 
		if pivot_prev != None and pivot_prev == start :
			self.sort(pivot_prev.next, end) 
			  
		# // if pivot is in between of the list, 
		# // start from next of pivot,  
		# // since we have pivot_prev, so we move two nodes 
		elif pivot_prev != None and pivot_prev.next != None :
			self.sort(pivot_prev.next.next, end) 

			
myLL = LinkedList() 
myLL.AddNode(10) 
myLL.AddNode(9) 
myLL.AddNode(7) 
myLL.AddNode(2) 
myLL.AddNode(8)
end = myLL.head
while end.next:
	end = end.next

myLL.sort(myLL.head,end)
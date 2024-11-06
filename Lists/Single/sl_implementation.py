class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self):
		self.head = None


	def insertAtFirst(self, new_data):
		if self.head == None:
			new_node = Node(new_data)
		else:
			new_node = Node(new_data)
			new_node.next = self.head
		self.head = new_node


	def insertAfter(self, prev_node, new_data):
		if prev_node == None:
			return

		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


	def append(self, new_data):
		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None

		new_node = Node(new_data)
		# 4. If the Linked List is empty, then make the
		#    new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next =  new_node


	# Given a reference to the head of a list and a key,
	# delete the first occurence of key in linked list
	def deleteNode(self, key):

		# Store head node
		temp = self.head

		# If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted, keep track of the
		# previous node as we need to change 'prev.next'
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if key was not present in linked list
		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None

	def deleteMiddle(self):
		if self.head.next is None:
			self.head = None
			return
		slow, fast = self.head, self.head
		prev_slow = None

		while fast and fast.next:
			prev_slow = slow
			slow = slow.next
			fast = fast.next.next

		prev_slow.next = slow.next
		slow = None
		return self.head


	def oddEvenList(self):
		if not self.head:
			return

		count = 1
		even = None
		odd = None
		evenHead = None
		startNode = self.head

		while startNode:
			# prev_node = startNode
			if count%2 != 0:
				if odd is None:
					odd = startNode
				else:
					odd.next = startNode
					odd = odd.next
			else:
				if even is None:
					even = startNode
					evenHead = startNode
				else:
					even.next = startNode
					even = even.next
			startNode = startNode.next
			count += 1
		odd.next= evenHead
		if even:
			even.next = None
		return self.head


	def reverseList(self):
		if not self.head:
			return

		curr = self.head
		prev = None

		while curr:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		self.head = prev


	def reverseList2(self, left, right):
		dummy = Node(0, self.head)

		leftPrev, curr = dummy, self.head
		for i in range(left - 1):
			leftPrev, curr = curr, curr.next

		prev = None
		for i in range(right - left + 1):
			tempNext = curr.next
			curr.next = prev
			prev, curr = curr, tempNext

		leftPrev.next.next = curr
		leftPrev.next = prev
		self.head = dummy.next

  	# Utility function to print the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next


# Code execution starts here
if __name__=='__main__':
	# Start with the empty list
	llist = LinkedList()
	# Insert 6.  So linked list becomes 6->None
	llist.append(6)
	# Insert 7 at the beginning. So linked list becomes 7->6->None
	llist.insertAtFirst(7)
	# Insert 1 at the beginning. So linked list becomes 1->7->6->None
	llist.insertAtFirst(1)
	# Insert 4 at the end. So linked list becomes 1->7->6->4->None
	llist.append(4)
	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
	llist.insertAfter(llist.head.next, 8)
	# llist.deleteMiddle()
	print('Created linked list is:')
	llist.printList()
	# llist.oddEvenList()
	# print('Created linked list is:')
	# llist.printList()
	# llist.reverseList()
	llist.reverseList2(2, 4)
	print('Created linked list is:')
	llist.printList()


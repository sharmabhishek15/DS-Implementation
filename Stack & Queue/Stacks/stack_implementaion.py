class Node:
    def __init__(self, data):
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

    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        else:
            popNode = self.head
            self.head = popNode.next
            popNode.next = None
            return popNode.data

    def top(self):
        if self.head == None:
            return None
        else:
            return self.head.data


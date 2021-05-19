class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insertAtFirst(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node


    def insertAfterNode(self, prev_node, new_data):
        if prev_node == None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next != None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist.insertAtFirst(5)
    llist.insertAtFirst(6)
    llist.insertAtEnd(11)
    llist.insertAtFirst(7)
    llist.insertAtFirst(8)
    llist.insertAfterNode(llist.head.next,10)
    llist.printList()
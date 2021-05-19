class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def removesDuplicates(self):
        temp = self.head

        while temp != None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp = new
            else:
                temp = temp.next


    def printList(self):
        while self.head != None:
            print(self.head.data)
            self.head = self.head.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    # Takes a sorted list.
    llist = LinkedList()
    llist.push(3)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(1)
    llist.removesDuplicates()
    llist.printList()
class Node:
    def __init__(self, data):
        self.data = data
        self.head = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end='')
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(6)
    llist.push(7)
    llist.push(1)
    llist.push(4)
    llist.printList()
    llist.deleteNode(7)
    llist.printList()

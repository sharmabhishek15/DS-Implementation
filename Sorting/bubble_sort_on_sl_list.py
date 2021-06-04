class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, start=None, count=0):
        self.head = start
        self.node_count = count


    def insertAtFirst(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.node_count += 1

    def bubbleSort(self):
        prev = None
        current = self.head
        next = current.next
        for i in range(1,self.node_count-1):
            print("iteration : " , i)
            while current.next is not None:
                if current.data > next.data:
                    if prev == None:
                        prev = current.next
                        next = next.next
                        prev.next = current
                        current.next = next
                        self.head = prev
                    else:
                        temp = next
                        next = next.next
                        prev.next = current.next
                        prev = temp
                        temp.next = current
                        current.next = next
                else:
                    prev = current
                    current = next
                    next = current.next

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist.insertAtFirst(7)
    llist.insertAtFirst(2)
    llist.insertAtFirst(4)
    llist.insertAtFirst(6)

    print('Created linked list is:')
    llist.printList()
    print('Bubble Sort:')
    llist.bubbleSort()
    llist.printList()


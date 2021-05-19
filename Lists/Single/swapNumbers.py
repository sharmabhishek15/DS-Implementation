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


    def swapNumbers(self,x , y):
        prev_to_x = None
        curr_x = self.head
        prev_to_y = None
        curr_y = self.head

        while curr_x != None and curr_x.data != x:
            prev_to_x = curr_x
            curr_x = curr_x.next

        while curr_y != None and curr_y.data != y:
            prev_to_y = curr_y
            curr_y = curr_y.next

        if prev_to_x != None:
            prev_to_x.next = curr_y
        else:
            self.head = curr_y

        if prev_to_y != None:
            prev_to_y.next = curr_x
        else:
            self.head = curr_x

        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp

    def printList(self,head):
        while head != None:
            print(head.data)
            head = head.next



if __name__ == '__main__':
    # Start with the empty list
    # Takes a sorted list.
    llist = LinkedList()
    llist.push(3)
    llist.push(4)
    llist.push(12)
    llist.push(34)
    llist.push(15)
    print_head = llist.head
    llist.printList(print_head)
    print("\n")
    llist.swapNumbers(12,34)
    llist.printList(print_head)
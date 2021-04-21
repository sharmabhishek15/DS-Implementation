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


    def checkPalindrome(self):
        slow_ptr = self.head
        prev_to_slow_ptr = self.head
        fast_ptr = self.head
        midnode = None
        # Initialize result
        res = True

        if self.head != None and self.head.next != None:
            while fast_ptr and fast_ptr.next:
                prev_to_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next

            second_half = slow_ptr

            # Set None last node of first half
            prev_to_slow_ptr.next = None

            # Reverse the second half
            second_half = self.reverse(second_half)
            # Compare
            res = self.compareLists(self.head, second_half)

            # Construct the original list back
            # Reverse the second half again
            second_half = self.reverse(second_half)

            if (midnode != None):

                # If there was a mid node (odd size
                # case) which was not part of either
                # first half or second half.
                prev_to_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_to_slow_ptr.next = second_half
        return res

    # Function to check if two input
    # lists have same data
    def compareLists(self, head1, head2):

        temp1 = head1
        temp2 = head2

        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0

        # Both are empty return 1
        if (temp1 == None and temp2 == None):
            return 1

        # Will reach here when one is NULL
        # and other is not
        return 0


    def reverse(self,node):
        prev = None
        current = node
        next = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev



# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(2)
    llist.push(1)
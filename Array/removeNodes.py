def removeNodes(head, k):
    """
        Problem Statement
        You are given a Singly Linked List of integers and an integer 'K'. Your task is to remove all such nodes from the linked list whose value is equal to 'K'.
        A singly linked list is a linear data structure in which we can traverse only in one direction i.e., from Head to Tail. It consists of several nodes where each node contains some data and a reference to the next node.
        Sample Input 1:
        2 5 7 10 -1
        7
        4 9 10 -1
        3
        2 2 2 1
        2
        Sample Output 1:
        2 5 10 -1
        4 9 10 -1
        1
    """
    # Write your code here.

    temp = head
    prev = head
    while temp:
        if head.data == k:
            newHead = head.next
            prev = newHead
            head = newHead
            newHead = None
        else:

            if temp.data == k:
                prev.next = temp.next
            else:
                prev = temp
        temp = temp.next

    return head
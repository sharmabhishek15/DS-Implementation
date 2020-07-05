# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.
#
# Implement the DinnerPlates class:
#
# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
# int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
# int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
# Example:
#
# Input:
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output:
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
#
# Explanation:
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 4.  The stacks are now:   1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 3.  The stacks are now:   1
#                                                         ﹈
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
class DinnerPlates:
    listOfStacks = []
    popStack = []

    def __init__(self, capacity: int):
        self.len = capacity

    def push(self, val: int):
        if len(self.listOfStacks) == 0:
            stack = []
            stack.append(val)
            self.listOfStacks.append(stack)
        else:
            if len(self.popStack) == 0:
                temp = self.listOfStacks[-1]
                if len(temp) < self.len:
                    temp.append(val)
                elif len(temp) == self.len:
                    stack = []
                    stack.append(val)
                    self.listOfStacks.append(stack)
            else:
                self.popStack.sort()
                print(self.popStack.sort())
                i = self.popStack[0]
                print(i, self.listOfStacks)
                temp = self.listOfStacks[i]
                temp.append(val)
                self.popStack.pop(0)

    def pop(self):
        if len(self.listOfStacks) >= 1:
            rightStack = self.listOfStacks[-1]
            if len(rightStack) == 1:
                rightStack.pop()
                return self.listOfStacks.pop()
            else:
                return rightStack.pop()
        else:
            return -1

    def popAtStack(self, index: int):
        if len(self.listOfStacks) >= 1:
            self.popStack.append(index)
            leftStack = self.listOfStacks[index]
            if len(leftStack) == 1:
                leftStack.pop()
                return self.listOfStacks.pop()
            else:
                return leftStack.pop()
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
D.popAtStack(0)
D.push(20)
D.push(21)
D.popAtStack(0)
D.popAtStack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()
class DinnerPlates:
    listOfStacks = []
    popStack = []

    def __init__(self, capacity: int):
        self.len = capacity

    def push(self, val: int):
        if len(self.listOfStacks) == 0:
            popStack = []
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
                i = self.popStack[0]
                temp = self.listOfStacks[i]
                temp.append(val)
                self.popStack.pop(0)

    def pop(self):
        if len(self.listOfStacks) >= 1:
            rightStack = self.listOfStacks[-1]
            if len(rightStack) == 1:
                rm = len(self.listOfStacks) - 1
                if rm in self.popStack:
                    ind = self.popStack.index(rm)
                    self.popStack.pop(ind)
                r = rightStack.pop()
                self.listOfStacks.pop()
                return r
            else:
                return rightStack.pop()
        else:
            return -1

    def popAtStack(self, index: int):

        if len(self.listOfStacks) >= 1:
            if index not in self.popStack:
                self.popStack.append(index)
            leftStack = self.listOfStacks[index]
            if len(leftStack) == 1:
                r = leftStack.pop()
                self.listOfStacks.pop(index)
                return r
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
D.popAtStack(1)
D.popAtStack(1)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()

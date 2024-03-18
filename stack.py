class Stack:

    def __init__(self) -> None:
        self.stack = [None] * 2
        self.capacity = len(self.stack)
        self.index = 0


    def add(self,x):
        if self.index == self.capacity:
            self.resize()
        self.stack[self.index] = x
        self.index += 1

        
        return self.stack
    def pop(self):
        temp = self.stack[self.index-1]
        self.stack[self.index-1] = None
        self.index = max(0,self.index -1 )
        print(temp)
        return self.stack

    def resize(self):
        temp = [None] * (self.capacity * 2)

        for i in range(len(self.stack)):
            temp[i] = self.stack[i]

        self.stack = temp
        self.capacity *= 2

stack = Stack()

for i in range(10):
    command,number = list(map(int,input().split()))

    if command == 1:
        print(stack.add(number))

    else: print(stack.pop())
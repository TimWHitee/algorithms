class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def add(self, x):
        n = Node(x)
        if self.top:
            n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
    
stack = Stack()

while True:
    try :
        cmd = input()
        
        if cmd != '0':
            stack.add(int(cmd))
            print(f'Added {cmd} \n')
            
        else:
            
            print(f'Popped: {stack.pop()}')

    except KeyboardInterrupt:
        print('Program was stopped!')
        break


        
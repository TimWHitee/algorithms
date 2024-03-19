class Node:
    def __init__(self,value = None):
        self.value = value

        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self,x):
        n = Node(x)
        
        if self.head is None:
            self.head = n
        else: 
            self.tail.next = n
        self.tail = n
            
    def pop(self):
        if self.head is not None:
            x =  self.head.value
            self.head = self.head.next
            return x
        else: None

queue = Queue()
while True:
    try :
        cmd = input()
        
        if cmd != '0':
            queue.add(int(cmd))
            print(f'Added {cmd} \n')
            
        else:
            
            print(f'Popped: {queue.pop()}')

    except KeyboardInterrupt:
        print('Program was stopped!')
        break
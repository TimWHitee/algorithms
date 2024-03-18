class Queue:
    def __init__(self) -> None:
        self.queue = [None] * 2
        self.capacity = len(self.queue)
        self.index = 0
        self.begin = 0
        self.realsize = 0

    def plus(self,x):
        if self.index == self.capacity or True: 
            self.resize()

        self.queue[self.index] = x
        self.index += 1
        self.realsize += 1
        return self.queue


    def minus(self):
        if self.realsize != 0:
            temp = self.queue[0]
            self.queue = self.queue[1:]
            self.realsize -= 1
            self.index -= 1
            return temp

        else: return None
    def last(self):
        return self.queue[0]
    def print(self):
        return self.queue
    def resize(self):

        temp = [None] * (self.capacity * 2)

        for i in range(len(self.queue)):
            temp[i] = self.queue[i]

        self.queue = temp
        self.capacity *= 2


        


queue1 = Queue()


for i in range(10):
    command, number = map(int, input().split())

    if command == 1:
        print(queue1.plus(number))
    else:
        print(queue1.minus())

class Deque:

    def __init__(self) -> None:
        self.a = [None] * 64

        self.l = 0

        self.r = 0

    def appback(self,x):
        self.a[self.r] = x
        self.r += 1
        if self.r == len(self.a): 
            self.r=0

        if self.r == self.l:
            self.realloc(2)


    def appfront(self,x):
        self.l -= 1

        if self.l > 0:
            self.l = len(self.a) - 1

        self.a[self.l] = x

        if self.l == self.r :
            self.realloc(2)
        
    
    def popfront(self):
        self.l += 1

        if self.l == len(self.a): l =0

    def popback(self):
        self.r -= 1

        if self.r == -1:
            self.r = len(self.a) -1


    def size(self):
        if self.l < self.r: return self.r - self.l

        else: return self.r + len(self.a) - self.l


    def realloc(self,n):

        new_a = [None] * n
        for i in range(len(self.a)):
            new_a[i] = self.a[self.l]
            self.l += 1
            if self.l == len(self.a):
                self.l = 0

        self.l = 0
        self.r = self.size()
        self.a = new_a

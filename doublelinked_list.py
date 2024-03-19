class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_after(self, i, x):  # добавить узел после i со значением x
        if i is None:
            return
        n = Node(x)
        n.next = i.next
        if i.next:
            i.next.prev = n
        i.next = n
        n.prev = i
        if n.next is None:
            self.tail = n

    def remove_node(self, i):  # удалить узел, следующий за i
        if i is None or i.next is None:
            return
        i.next = i.next.next
        if i.next:
            i.next.prev = i
        else:
            self.tail = i

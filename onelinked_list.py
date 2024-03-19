class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_after(self, i, x):  # добавить узел после i со значением x
        if i is None:
            return
        n = Node(x)
        n.next = i.next
        i.next = n

    def remove_node(self, i):  # удалить узел, следующий за i
        if i is None or i.next is None:
            return
        i.next = i.next.next

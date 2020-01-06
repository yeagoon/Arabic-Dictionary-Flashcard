class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        if self.head.data is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def display(self):
        elms = []
        cur = self.head
        while cur is not None:
            elms.append(cur.data)
            cur = cur.next
        print(elms)

    def display_number(self, number):
        cur = self.head
        while number > 1:
            cur = cur.next
            number = number - 1
        return cur

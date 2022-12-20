# implement single list
#
# Path: Tydzien 9/single_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SingleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        if self.is_empty():
            return 0
        else:
            counter = 1
            node = self.head
            while node.next is not None:
                counter += 1
                node = node.next
            return counter

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("Empty List")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Empty List")
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return node

    def join(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        elif not other.is_empty():
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        other.clear()

    def clear(self):
        while not self.is_empty():
            self.remove_head()

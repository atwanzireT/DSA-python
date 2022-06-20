class Node:
    """Node class"""
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    """Linked list class"""
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        """Node class object"""
        self.head = Node(data, self.head )
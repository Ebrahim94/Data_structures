class DoubleNode:
    def __init__(self, value):
        self.previous =  None
        self.value =  value
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = DoubleNode.value(value)
            self.tail = self.head
            return
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            return
        
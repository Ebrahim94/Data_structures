class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.size())
print(q.is_empty())

print(q.head.value)
print(q.dequeue())
print(q.head.value)
print(q.dequeue())
print(q.head.value)

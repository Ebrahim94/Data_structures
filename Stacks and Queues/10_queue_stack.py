class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.stack = Stack()

    def size(self):
        return self.stack.size()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        temp_stack = Stack()
        temp_stack_second = Stack()

        for i in range(self.size() - 1):
            temp_stack.push(self.stack.pop())
        
        for i in range(temp_stack.size()):
            temp_stack_second.push(temp_stack.pop())
        
        dequeued_value = self.stack.pop()
        self.stack = temp_stack_second

        return dequeued_value

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
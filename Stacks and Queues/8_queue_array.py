class Queue:
    def __init__(self, queue_size:int = 10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0
    
    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0
    
    def front(self):
        if self.front_index == -1:
            return None
        else:
            return self.arr[self.front_index]
    
    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value
    
    def _handle_queue_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) * 2)]

        index = 0

        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.front())
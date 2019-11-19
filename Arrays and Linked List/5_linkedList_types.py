class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    


head = Node(3)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node  = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return
    
    def to_list(self):
        node = self.head
        python_list = []

        while node:
            python_list.append(node.value)
            node = node.next
        
        return python_list


linked = LinkedList()

linked.append(1)
linked.append(2)
linked.append(3)

node = linked.head

while node:
    print(node.value)
    node = node.next

print(linked.to_list())
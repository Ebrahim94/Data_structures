# Create a node that take a value and points to the next Node in memory
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# create a linked list stack
class Stack(object):
    def __init__(self):
        self.head = None
        self.num_elements = 0

    # Add the push method
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next  = self.head
            self.head = new_node

        self.num_elements += 1

    #remove the last node to enter the stack
    def pop(self):
        if self.head == None:
            return self.head

        value = self.head.value
        self.head = self.head.next
        self.num_elements -=1
        return value

    #return the number of Nodes in the linked list
    def size(self):
        return self.num_elements

    #check if the number of elements is empty
    def is_empty(self):
        return self.num_elements == 0

foo = Stack()
print(foo.is_empty())
foo.push(1)
foo.push('i am the second Node')
foo.push('this is stored in a different place in memory than the other nodes')


print(foo.size())
print(foo.head.value)

print(foo.pop())
print(foo.pop())

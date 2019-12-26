#A node of a Linked List
class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating a stack with different methods that we can use to manipulate the linked list
class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        value = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def top(self):
        if self.head is None:
            return None
        return self.head.data

#this is a very easy way to reverse a stack
def reverse_stack(stack):
    #initalize a new stack
    inv_stack = Stack()

    #while the last element to be inputed has a value we are going to iterate over the elements
    while stack.top() is not None:
        #for each element we are going to add it to this new stack
        inv_stack.push(stack.pop())
    #doing this will reverse a stack since the last element in this new stack is the first element
    #in the stack that's the argument of this function
    return inv_stack


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

def lazy_print(stack):
    current = stack.head

    while current:
        print(current.data)
        current = current.next


lazy_print(stack)

lazy_print(reverse_stack(stack))

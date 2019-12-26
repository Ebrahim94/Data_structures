class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        retrun self.num_elements == 0

    def pop(self):
        if is_empty():
            return None
        value = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return value
    
    def top(self):
        if self.head is None:
            return None
        return self.head.data

def minimum_bracket_reversal(input_string):
    extra_movements = 0

    #if the first element in input_string is a closing bracket then reverse it and increment the number of movements
    if input_string[0] == '}':
        input_string = '{' + input_string[1:]
        extra_movements +=1 

    #if the last element in input_string is an opening bracket then reverse it
    if input_string[len(input_string)-1] == '{':
        input_string = input_string[:len(input_string) -1] + '}'
        extra_movements += 1

    prev_char = '_'

    #if the input string is not divisible by 2 then this input string is not reversable
    if len(input_string) % 2 != 0:
        return -1
    else:
        stack = Stack()

        for char in input_string:
            if prev_char + char = "{}":
                _ = stack.pop()
                prev_char = stack.top()

                if stack.size() == 0:
                    prev_char = '_'
            else:
                stack.push(char)
                prev_char = char

    



            
#create a Linked List class that takes in a value and points to the location of the next Node in memory
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#a stack of linked lists
class Stack:
    #initalize the stack with two variables assigned to the instance one being the head of the linked list
    # the other being the number of elements that is in this Linked List
    def __init__(self):
        self.num_elements = 0
        self.head = None

    #Here we are going to push Nodes onto a Linked List
    def push(self,data):
        #the node that we are going to push into a linked list
        new_node = LinkedListNode(data)

        #if there are no elements in the stack set the new element as the head
        if self.head == None:
            self.head = new_node
        else:
            #else the new node will reference the old head
            new_node.next = self.head
            #and then replace it
            self.head = new_node

        #the number of elements in this stack has increased by one
        self.num_elements += 1
    
    #does a check to see if the stack is empty
    def is_empty(self):
        self.num_elements == 0

    #remove the last inputed element from the stack are return it 
    def pop(self):
        #if the stack is empty it should return None
        if self.is_empty():
            return None
        
        #the last element to enter the stack
        temp = self.head.data
        #remove this Node from the stack
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        #if the top most element of the stack does not exist return None
        if self.head is None:
            return None
            #if it does exist return data
        return self.head.data

    def size(self):
        return self.num_elements


#so the input is going to be of type list 
def evaluate_post_fix(input_list):
    stack = Stack()

    for element in input_list:
        if element in ['+', '-', '*', '/']:
            element_2 = stack.pop()
            element_1 = stack.pop()
            stack.push(str(int(eval(element_1 + element + element_2))))
        
        else:
            stack.push(element)

    return stack.pop()

print(evaluate_post_fix(["1", "2", "+", "3", "+"]))
class Stack(object):
    # initialize the class with 3 variables and one will be an array with
    # initial size of 10 while the other two will be set to 0
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    # add an element to the arr variable
    def push(self, data):
        if self.next_index == len(self.arr):
            print("out of space")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements +=1

    # remove that last inputed element in the stack
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None

        self.next_index -=1
        self.num_elements -=1
        return self.arr[self.next_index]
        
    # Add the size method
    def size(self):
        return self.num_elements
    
    #checks to see if the stack is empty
    def is_empty(self):
        return self.next_index == 0

    #if the array limit has reached then execute this function
    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        # double the size of the array
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

# create a stack with the name foo
foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10)
foo.push(11)
print (foo.pop())
print(foo.arr)

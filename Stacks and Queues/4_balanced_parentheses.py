# simple stack using python's built in methods
class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if size() == 0:
            return None
        return self.items.pop()

def equation_checker(equation):
    #A stack is an instance of class Stack
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop == None:
                return False
    
    if stack.size() == 0:
        return True
    else:
        return False

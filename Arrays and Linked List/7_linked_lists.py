class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,value):
        # Add a value to the beginning of the list
        if self.head == None:
            self.head == Node(value)
        else:
            previous_head = self.head
            self.head = Node(value)
            self.head.next = previous_head

    def append(self, value):
        #Add a value to the end of the list
        tail = self.head

        if tail is None:
            self.head = Node(value)
        else:
            while tail.next:
                tail = tail.next

                tail.next = Node(value)
    
    def search(self, value):
        #Search the linked list for a value and return the node
        node = self.head
        while node.next:
            if node.value == value:
                return value
            value = value.next
        
        return None



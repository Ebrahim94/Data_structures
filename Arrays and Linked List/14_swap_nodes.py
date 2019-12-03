class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list):
        self.head = None

        for element in init_list:
            self.append(element)
    
    def append(self, value):

        if self.head == None:
            self.head = Node(value)
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = Node(value)

def swap_nodes(head, left_index, right_index):
    node = head
    position = 0

    while position <= right_index:
        if position == left_index:
            left_value = node.value
        
        if position == right_index:
            right_value = node.value
        
        position += 1
        node = node.next

    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            node.value = right_value

        if position == right_index:
            node.value = left_value

        position += 1
        node = node.next

    return head

LinkedList([1,2,3,4,5,6])
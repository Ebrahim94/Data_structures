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

        position_tail = self.head
        while position_tail.next:
            position_tail = position_tail.next

        position_tail.next= Node(value)



def print_list(linked_list):
    tail_position = linked_list
    while tail_position:
        print(tail_position.value)
        tail_position = tail_position.next

a = LinkedList([1,2,3,4,5,6])

print_list(a.head)
        




def skip_i_delete_j(head, i ,j):
    node = head
    trim_list = None

    counter = 1
    i_mode = True
    last_node = False

    while not last_node:
        if i_mode:
            if trim_list is None:
                trim_list = Node(node.value)
            else:
                position_tail = trim_list
                while position_tail.next:
                    position_tail = position_tail.next
                position_tail.next = Node(node.value)

            if counter == i:
                i_mode = False
                counter = 0

        else:
            if counter == j:
                i_mode = True
                position_counter = 0

        counter += 1
        last_node = node.next is None
        node = node.next
        
    return trim_list

print_list(skip_i_delete_j(a.head, 2,2))
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
# append to a list
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(value)

# generator function
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next


# prepend to a linked list a particular value

def insert_at_head(linked, value):
    continuity = linked.head
    linked.head = Node(value)
    linked.head.next = continuity

    return linked


# reverse the linked list
def reverse(Linked_List):
    tail_position = Linked_List.head
    reversed_linked_list = LinkedList()

    while tail_position is not None:
        value = tail_position.value
        reversed_linked_list = insert_at_head(reversed_linked_list, value)
        tail_position = tail_position.next

    return reversed_linked_list

#append to the list
a = LinkedList()
a.append(2)
a.append(4)
a.append(6)

#print the linked list
def print_list(linked):

    node = linked.head
    while node:
        print(node.value)
        node = node.next


print_list(reverse(a))
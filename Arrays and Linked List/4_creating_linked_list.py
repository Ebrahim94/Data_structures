#Creating a node of a linked list
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#Integer values to be stored in each Node
values = [1,2,3,4,5]


#creating a linked list
def create_linked_list(values):

    head = None
    tail = None

    for value in values:
        if head == None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head



head = create_linked_list(values)


#Prints out a linked list given the head of the list
def print_list(head):

    current_node = head

    while current_node != None:
        print(current_node.value)
        current_node = current_node.next


print_list(head)







# #Function that creates a linked list given a list of values
# def linked_list(values):

#     for i in range(len(values)):
#         if (i==0):
#             head = Node(values[i])
#             tail = head
#         else:
#             tail.next = Node(values[i])
#             tail = tail.next
        
#     return head

#
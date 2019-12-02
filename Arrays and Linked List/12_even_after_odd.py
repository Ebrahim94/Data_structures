class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def even_after_odd(head):
    linked_list_end = False
    even_linked_list = None
    odd_linked_list = None

    node = head

    while not linked_list_end:
        if node.value % 2 ==0: #even case
            if even_linked_list is None:
                even_linked_list = Node(node.value)
            else:
                position_tail = even_linked_list
                while position_tail.next:
                    position_tail = position_tail.next
                position_tail.next= Node(node.value)
        
        else:
            if odd_linked_list is None:
                odd_linked_list = Node(node.value)
            
            else:
                position_tail = odd_linked_list
                while position_tail.next:
                    position_tail = position_tailed.next
                
                position_tail.next = Node(node.value)

        linked_list_end = node.next is None
        node = node.next

    position_tail = odd_linked_list
    while position_tail.next:
        position_tail = position_tail.next
    
    position_tail.next = even_linked_list

    return odd_linked_list
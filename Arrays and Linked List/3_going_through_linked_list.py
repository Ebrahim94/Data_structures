#The Node Inherits from object this is automatically done in python 3 not in python 2
#This allow the Class to support various things that we are used to it supporting

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#Manually inseting values for the Node
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)


#Check all the values of the linked List
def check_list(node):

    current_node = node #the input of this function will be the head node

    while (current_node != None):
        print(current_node.value) #Prints out the value of the Current Node
        current_node = current_node.next #Updates the variable current_node to the next value of the list

check_list(head)
        

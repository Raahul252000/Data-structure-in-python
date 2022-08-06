# Singly linked list:
"""
singly linked list consist of nodes with one data field and one link/reference of next element.

common Operations on singly linkedlist:
1. Adding elements to the list:
        a. in the beginning.
        b. in the end.
        c. inbetween.
            - add after the node.
            - add before the node.
2. Removing element from the list:
    a. from the beginning.
    b. from the end.
    c. from between.
3. Traversal.
"""

# creating node class to create individual node.
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def print_ll(self):
        """
        with this method we can traverse through all the nodes of the linkedlist and print the data from the data field
         of nodes.
        """
        if self.head == None:
            print("Linkedlist is empty.")
        else:
            n = self.head
            while n != None: 
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        """
        this method is creating new node and adding that node at the beginning of the linked list.
        """
        new_node = Node(data)   # creating new node.
        new_node.ref = self.head    # pointing next of new node to 1st node.
        self.head = new_node    # pointing head to new node.
        # head always contains the address of the first node therefore we are storing address of first node into the reference field of the new_node, so it will link new_node with 1st node.

    def add_end(self,data):
        """
        this method will create new node and add that node at the end of the linked list.
        """
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node


ll1 = Linkedlist()   # creating linked list with no node.
ll1.print_ll()
ll1.add_end(35)
ll1.add_end(45)
ll1.add_begin(10)
ll1.add_begin(20)
ll1.print_ll()

# singly linked list.
"""
IN this code, we will see how to add new node inbetween after the node or before the node.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("Empty linked list.")
        else:
            n = self.head
            while n.ref is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n != None:
                n = n.ref
            n.ref = new_node

    def add_after_node(self,data,x):
        n = self.head
        while n.ref != None:
            if x == n.data:
                break
            n = n.ref
        if n == None:
            print("Node is not present in the linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


ll1 = Linkedlist()

ll1.print_LL()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(50)
ll1.add_end(60)
ll1.print_LL()
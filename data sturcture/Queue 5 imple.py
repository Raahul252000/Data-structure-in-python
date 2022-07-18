# Implementing queue using example:

import collections
queue1 = collections.deque()

def enqueue():
    element = int(input("enter the element: "))
    queue1.appendleft(element)
    print(f"{element} is enqueued into the queue.")

def dequeue():
    if not queue1:
        print("queue is empty.")

    else:
        a = queue1.pop()
        print(f"{a} is dequeued from the list.")

def display():
    print(queue1)

def head_element():
    print(queue1[-1]," is at the head of the queue.")

def tail_element():
    print(queue1[0]," is at the tail of the queue.")

while True:
    choice = int(input("Press, 1.enqueue, 2.dequeue, 3.display, 4.head element, 5.tail element and 6.quit: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        head_element()
    elif choice == 5:
        tail_element()
    elif choice == 6:
        break

# implementing stack using queue module:
"""
Queue module also has a LIFOQueue, which is basically a Stack. Data is inserted into Queue using the put() function
and get() takes data out from the Queue.

There are various functions available in this module:

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default),
then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.

"""
#
# import queue
# stack = queue.LifoQueue()
# print(stack)
# print(stack.qsize())
#
# # insert the elements
# stack.put(23)
# stack.put(55)
# stack.put(12)
# stack.put(34)
# stack.put(67)
#
# # check the lenght of stack
# print(stack.qsize())
#
# # pop the element
# print(stack.get())
# print(stack.get())
# print(stack.get())
# print(stack.get())
# print(stack.get())
# print(stack.qsize())
#
# # check if the stack is empty
# print(stack.empty())

# Example 1:
import queue
stack = queue.LifoQueue()

def push():
    element = int(input("Enter the element:"))
    stack.put(element)

def pop_element():
    if stack.qsize() == 0:
        print("stack is empty")
    else:
        stack.get()

def stack_size():
    print(stack.qsize())

while True:
    choice = input("Press 1 to push, Press 2 to pop, Press 3 to check the size of the stack and Press 4 to quit() : ")
    if choice == "1":
        push()
    elif choice == "2":
        pop_element()
    elif choice == "3":
        stack_size()
    elif choice == "4":
        break
    else:
        print("Enter the valid input.")

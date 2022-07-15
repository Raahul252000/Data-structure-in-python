# implementing stack using collection module:
"""
In collection module there is a class called deque and we can use deque class as the stack.
'deque' stands for double ended queue. Here we can add the elements from both the sides. there are different methods to
to add the elements both the side. but stack works in LIFO  order, so we need only one end to add and remove the element.
so using few methods of deque class we can create the stack.

method:
to push = append()
to pop = pop()

"""
# import collections
# stack = collections.deque()
#
# # pushing elements
# stack.append(8)
# stack.append(12)
# stack.append(15)
# stack.append(19)
# print(stack)
#
# # checking whether the stack is empty or not:
# print(len(stack))
#
# # check the top element (last inserted) of the stack:
# print(stack[-1])
#
# # remove the elements from the stack:
# stack.pop()
# print(stack)

# Example:
import collections
stack = collections.deque()

def push():
    element = int(input("Enter the element: "))
    stack.append(element)
    print(stack)
def pop_element():
    if len(stack) == 0:
        print("stack is empty.")
    else:
        stack.pop()
    print(stack)

while True:
    choice = input("Press 1 to push, Press 2 to pop and Press 3 to quit: ")
    if choice == "1":
        push()
    elif choice == "2":
        pop_element()
    elif choice == "3":
        break
    else:
        print("Enter the valid input.")

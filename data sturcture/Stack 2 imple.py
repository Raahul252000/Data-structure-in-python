# implementing stack using list:

stack = []
def push():
        element = int(input("enter the element: "))
        stack.append(element)
        print(stack)

def pop_element():
    if len(stack) == 0:
        print("Stack is already empty.")
    else:
        stack.pop()
        print("element removed.")
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

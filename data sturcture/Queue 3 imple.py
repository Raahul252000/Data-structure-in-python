# Implementing queue with example:
queue = []
def enqueue():
    element = int(input("enter the element of the queue: "))
    queue.append(element)
    print(element, "added into the queue.")

def dequeue():
    if not queue:
        print("queue is empty.")
    else:
        r = queue.pop(0)
        print(r,"is removed.")

def display():
    print(queue)

while True:
    choice = int(input("press 1.enqueue, 2.dequeue, 3.display and 4.quit: "))
    if choice == 1:
        enqueue()
    if choice == 2:
        dequeue()
    if choice == 3:
        display()
    if choice == 4:
        break
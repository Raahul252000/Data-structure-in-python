# Implementing Queue using list:
"""
Q: as we know that in queue first element added in queue is removed first(FIFO), but if we use the list then stack will be
created then how to solve this problem?
Ans: at the time of removing we will use the index from zero(0), this is how we will be able to remove the elements from
the head side.
"""
# adding elements from the right/back side and removing element from left/front side.
    # To enqueue element -- append()
    # To dequeue element -- pop(0)
Queue = []

# Enqueue
Queue.append(10)
Queue.append(20)
Queue.append(30)
Queue.append(40)
Queue.append(50)

print(Queue)

# Dequeue: 0 index will remove the elements from the head/front.
Queue.pop(0)
print(Queue)
Queue.pop(0)
Queue.pop(0)
print(Queue)

# we can also add elements from the left/face end and remove elements form the right/back end. we can use any way to use Queue.
    # To enqueue element -- insert()
    # To dequeue element -- pop().

queue2 = []

# Enqueue
queue2.insert(0,100)
queue2.insert(0,200)
queue2.insert(0,300)
queue2.insert(0,400)
queue2.insert(0,500)

print(queue2)

# Dequeue
queue2.pop()
queue2.pop()
queue2.pop()

print(queue2)

# to check if the queue is empty or not, use 'not nameofqueue'.
print(not queue2)
print(len(queue2))   # if the length is not 0 then it means that the queue is not empty.

# To check the length of queue use len() method:
print(len(Queue))

# to check the rear/back element at the queue: queue[-1]
print(queue2[-1])

# to chech the front/head element at the queue: queue[0]
print(queue2[0])
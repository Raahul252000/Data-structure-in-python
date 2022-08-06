# Implementing priority Queue using queue module (PriorityQueue class)

"""
By default, the PriorityQueue class of queue module gives the higher priority to lower values of the element.

setting priority as element itself.
"""

from queue import PriorityQueue
q1 = PriorityQueue()

# Enqueue
q1.put(20)
q1.put(50)
q1.put(30)
q1.put(10)
q1.put(40)
print(q1)

# Dequeue
print(q1.get_nowait())
print(q1.get_nowait())
print(q1.get_nowait())

# size of queue
print(q1.qsize())

"""
setting priority by appending tuple which contain value and its priority:
"""
q2 = PriorityQueue()

# Enqueue
q2.put((4,"apple"))
q2.put((3,"orange"))
q2.put((5,"Pineapple"))
q2.put((1,"Kiwi"))
q2.put((2,"banana"))

# Dequeue
print(q2.get_nowait())
print(q2.get_nowait())

#
print(q2.qsize())
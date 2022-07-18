# Implementing Queue using queue module (Queue class):
"""
queue is built-in module of Python which is used to implement Queue.
queue.Queue(maxsize) initializes a variable to a maximum size of maxsize.
A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule.

There are various functions available in this module:

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default),
then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.

Note: we can specify the size of the queue:
"""

import queue
queue1 = queue.Queue(8)   # size of the queue = 8
print(queue1.empty())

# the queue will full only if we provide the size of the queue at the time of creation.
print(queue1.full())

# Enqueue
queue1.put_nowait(10)
queue1.put_nowait(20)
queue1.put_nowait(30)
queue1.put_nowait(40)

# check the size of the queue
print(queue1.qsize())

# what is maxsize of the queue:
print(queue1.maxsize)

# Dequeue
queue1.get_nowait()
queue1.get_nowait()
queue1.get_nowait()

print(queue1.qsize())


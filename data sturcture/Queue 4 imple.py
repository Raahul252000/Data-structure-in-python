# Implementing Queue using collection module (deque class)
"""
Queue in Python can be implemented using deque class from the collection module. Deque is preferred over list in the
cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1)
time complexity for append and pop operations as compared to list which provides O(n) time complexity.

collection module provides methods to insert and removed data from both the end. means we can insert the data from the
right side as well as from the left side. similarly, we can remove data from both left and right side.

"""

# inserting data from left side and removing from right side.

       # to enqueue data -- appendleft()
       # to dequeue data -- pop()
import collections
queue = collections.deque()

# Enqueue
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)
queue.appendleft(50)            # deque([50,40,30,20,10])

# Dequeue
queue.pop()
queue.pop()                     # deque([50,40,30])

print(queue)

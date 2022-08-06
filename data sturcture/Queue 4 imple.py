# Implementing Queue using collections module (deque class)
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
queue1 = collections.deque()

# Enqueue
queue1.appendleft(10)
queue1.appendleft(20)
queue1.appendleft(30)
queue1.appendleft(40)
queue1.appendleft(50)            # deque([50,40,30,20,10])

# Dequeue
queue1.pop()
queue1.pop()                     # deque([50,40,30])

print(queue1)

# inserting elements from right side and removing from right left side.
        # To enqueue data -- append()
        # To dequeue data -- popleft()

queue2 = collections.deque()

# Enqueue
queue2.append(100)
queue2.append(200)
queue2.append(300)
queue2.append(400)
queue2.append(500)          # deque([100,200,300,400,500])

# Dequeue
queue2.popleft()
queue2.popleft()
queue2.popleft()            # deque([400,500])


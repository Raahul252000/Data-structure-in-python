# Implementing priority queue using list.

"""
setting priority as the element itself.
"""
pq1 = []

# Enqueue
pq1.append(10)
pq1.append(30)
pq1.append(50)
pq1.append(20)
print(pq1)

# setting the priority
pq1.sort()               # we set the priority as the lower element.
print(pq1)

# to set the priority as the higher element we can use sort(reverse=True)
# pq1.sort(reverse=True)
# print(pq1)

# Dequeue
pq1.pop(0)
pq1.pop(0)
print(pq1)           # [30,50]

"""
# setting priority by appending tuple which consist priority and element
"""

pq2 = []

# Enqueue: (priority,value)
pq2.append((1,"alexa"))
pq2.append((4,"siri"))
pq2.append((2,"Max"))
pq2.append((3,"sam"))           #[(1, 'alexa'), (4, 'siri'), (2, 'Max'), (3, 'sam')]
print(pq2)

# setting the priority as ascending order
pq2.sort()                      #[(1, 'alexa'), (2, 'Max'), (3, 'sam'), (4, 'siri')]
print(pq2)

# Dequeue
pq2.pop(0)
pq2.pop(0)
print(pq2)                     # [(3, 'sam'), (4, 'siri')]
# Day 20 - Queue using List

queue = []  # empty list for queue

# Enqueue (add element)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueues:", queue)

# Dequeue (remove element from front)
if len(queue) > 0:
    queue.pop(0)
    print("Queue after dequeue:", queue)
else:
    print("Queue is empty, cannot dequeue")

# Peek (see first element)
if len(queue) > 0:
    print("Front element:", queue[0])
else:
    print("Queue is empty, nothing to peek")

# Check if empty
print("Is queue empty?", len(queue) == 0)
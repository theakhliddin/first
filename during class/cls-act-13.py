# Queue operations and resulting state:
# Initial Queue: []
# enqueue(5) -> [5]
# enqueue(8) -> [5 , 8]
# dequeue() -> [8]
# enqueue(3) -> [8, 3]
# dequeue() -> [3]
# enqueue(1) -> [3 ,1]


size = 5

last_index = 4
next_value  = (last_index + 1) / size
print(next_value)
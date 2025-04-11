class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("John", 30)
p2 = Person("Jane", 25)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)




# push(5) - [5]
# push(8) - [5, 8]
# pop() - [5]
# push(3) - [5, 3]
# pop() - [5]
# push(1) - [5, 1]




# enque(5) - [5]
# enque(8) - [5, 8]
# deque() - [8]
# enque(3) - [8, 3]
# deque() - [3]
# enque(1) - [3, 1]
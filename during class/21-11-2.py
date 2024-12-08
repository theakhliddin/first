class Node:
    __slots__ = ('value', 'next')

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

class Stack:
    __slots__ = ['top', 'size']
    def __init__(self):
        self.top = None
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.size += 1 
    def pop(self):
        deleteNode = self.top.value
        self.top = self.top.next
        self.size -= 1
        return deleteNode
    
def main():
    stack = Stack()
    print(stack.is_empty())
    print("Initial size: ", stack.get_size())

    stack.push(10)
    stack.push(20)
    stack.push(20)

    print("Intital size: ", stack.get_size())
    deleteNode = stack.pop()
    print("Deleted Node: ", deleteNode)

    print("Current size, ", stack.get_size())
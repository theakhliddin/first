class Queue:
    def __init__(self):
        self.queue = []


    def enqueue(self,value):
        self.queue.append(value)

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue)==0 
    
    def _repr_(self):
        return repr(self.queue)
    def __str__(self):
        return str(self.queue)
    

q=Queue()
q.enqueue('s')
q.enqueue('n')

print(q)

    
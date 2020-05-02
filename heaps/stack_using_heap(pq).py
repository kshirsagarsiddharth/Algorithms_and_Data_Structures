import queue

class Stack:
    def __init__(self,number):
        self.PQ = queue.PriorityQueue(number)
        self.count = number

    def push(self,value):
        self.count -= 1
        self.PQ.put((self.count,value))
    
    def pop(self):
        return self.PQ.get()

class Queue:
    def __init__(self,number):
        self.PQ = queue.PriorityQueue(number)
        self.count = number

    def push(self,value):
        self.count += 1
        self.PQ.put((self.count,value))
    
    def pop(self):
        return self.PQ.get()




    


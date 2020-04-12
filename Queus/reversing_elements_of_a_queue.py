# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 06:10:43 2020

@author: siddharth
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:43:00 2020

@author: siddharth
"""

class Que:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.queue = [None] * capacity
        self.capacity = capacity
        
    # the queue is full when the size becomes equall to capacity
    def is_full(self):
        return  self.size == self.capacity
    
    # the  queue is empty when the size is equal to zero
    
    def is_empty(self):
        return self.size == 0
    
    # function to add an item to the queue
    # this changes the size and the rear of the queue
    def en_que(self,data):
        if self.is_full():
            print('the queue is full')
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print('The item enqueued to the queue is {}'.format(data))
        
    # function to remove the item from the queue
    def de_que(self):
        if self.is_empty():
            print('The queue is empty')
            return
        else:
            print('the item dequed is {}'.format(self.queue[self.front]))
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size = self.size - 1
        
        return temp
    
    def que_front(self):
        if self.is_empty():
            print('the queue is empty')
            return
        else:
            print('the front item is {}'.format(self.queue[self.front]))
    
    def que_rear(self):
        if self.is_empty():
            print('the queue is empty')
            return
        else:
            print('the rear of the queue is {}'.format(self.queue[self.rear]))
            

class Stack:
    
    
    # creating stack class and initializing the constructor
    def __init__(self,limit = 10):
        self.stk = []
        self.limit = limit
    # this function returns True if the stack(array) is empty else this 
    # function returns true
    def is_empty(self):
        return len(self.stk) <= 0
    
    def push(self,item):
        if len(self.stk) > self.limit:
            print('stack overflow')
        else:
            self.stk.append(item)
        print('stack after push -- >',self.stk)
    
    def pop(self):
        if len(self.stk) < 0:
            print('stack underflow')
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk) < 0:
            print('stack underflow')
            return 0
        else:
            return self.stk[-1]
        
    def size(self):
        return len(self.stk)
        
                                            
    
            


def reverse_elements_in_a_queue(stack,queue):
    queue.que_front()
    queue.que_rear()
    stack = Stack()
    while not queue.is_empty():
        
        stack.push(queue.de_que())
    while not stack.is_empty():
        queue.en_que(stack.pop())
    queue.que_front()
    queue.que_rear()
    

queue = Que(10)
stack = Stack()
for i in range(1,7):
    queue.en_que(i)

reverse_elements_in_a_queue(stack, queue)
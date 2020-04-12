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
            self.front = (self.front + 1) % self.capacity
            self.size = self.size - 1
    
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
            
qq = Que(100)
qq.en_que(10)
qq.en_que(20)
qq.que_front()
qq.que_rear()
qq.de_que()            
            



# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 03:18:26 2020

@author: siddharth
"""
class CircularQue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        
    def en_que(self,data):
        # condition for teh queue to be full
        if (self.rear + 1) % self.capacity == self.front:
            print('the queue is full')
           
        # condition for a empty queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = data
            
    def de_que(self):
        # condition for empty queue
        if self.front == -1:
            print('the queue is empty')
        # if the queue has one element
        elif (self.front == self.rear):
            print('{} is removed'.format(self.queue[self.front]))
            self.front = -1
            self.rear = -1
        else:
            print('{} is removed'.format(self.queue[self.front]))
            self.front = (self.front + 1) % self.capacity
    
    def que_front(self):
        if self.front == -1:
            print('the queue is empty') 
            return
        else:
            print('the front item is {}'.format(self.queue[self.front]))
    
    def que_rear(self):
        if (self.rear + 1) == self.front:
            print('the queue is empty')
            return
        else:
            print('the rear of the queue is {}'.format(self.queue[self.rear]))
            
                                                                
    
            
q = CircularQue(10)
q.en_que(10)
q.en_que(11)
q.en_que(12)
q.en_que(13) 

q.que_front()
q.que_rear()    
            


    
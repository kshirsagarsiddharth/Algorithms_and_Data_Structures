# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 03:06:08 2020

@author: siddharth
"""  
# in this implementation we assume that the rear is at index zero

class Deque:
    def __init__(self):
        self.de_que = []
    
    def enque_front(self,data):
        self.de_que.append(data)
    
    def enque_rear(self,data):
        self.de_que.insert(0,data)
    
    def deque_front(self):
        self.de_que.pop()
    
    def deque_rear(self):
        self.de_que.pop(0)
        
    def is_empty(self):
        return self.de_que == []
    
    def size(self):
        return len(self.de_que)
d = Deque()

d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
d.enque_front(10)
d.enque_rear(11)
print(d.size())

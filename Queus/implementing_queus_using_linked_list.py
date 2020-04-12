# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 04:45:19 2020

@author: siddharth
"""

class Node:
    def __init__(self,data):
        self.data  = data
        self.next = None

class Queue:
    def __init__(self):
        self.front,self.rear = None
        
    def is_empty(self):
        self.front == None
    
    def enque_ll(self,data):
        node = Node(data)
        if self.rear == None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
            
    def deque_ll(self):
        if self.is_empty():
            print('the list is empty')
            return
        print('the value to be dequed is {}'.format(self.front))
        self.front = self.front.next
        if self.front == None:
            self.rear = None
            
            
       
        
        
       
        
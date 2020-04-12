# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:35:58 2020

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

class Stack_costly_push:
    def __init__(self):
        self.que_one = Que(10)
        self.que_two = Que(10)
        self.current_size = 0
        # this variable is used to maintain the current number 
        # of elements
    def push(self,data):
        self.que_two.en_que(data)
        self.current_size += 1
        while (not self.que_one.is_empty()):
            self.que_two.en_que(self.que_one.de_que())
            print('pushing is done and swapping is started........')
            
        # swapping the name of the two queus
        self.q = self.que_one
        self.que_one = self.que_two
        self.que_two = self.q
    
    def pop(self):
        if self.que_one.is_empty():
            return
        temp = self.que_one.de_que()
        self.current_size -= 1
        print('the element popped from the stack is {}'.format(temp))
        return temp
    
    def top(self):
        if self.que_one.is_empty():
            return False
        else:
            return self.que_one.que_front()
            
            
        
'''One by one dequeue everything except the last element from q1 and enqueue to q2.
Dequeue the last item of q1, the dequeued item is result, store it.
Swap the names of q1 and q2
Return the item stored in step 2.
filter_none'''
            
class Stack_costly_pop:
    def __init__(self):
        self.que_one = Que(10)
        self.que_two = Que(10)
        self.current_size = 0
        
    def push(self,data):
        self.que_one.en_que(data)
        self.current_size += 1
    
    def pop(self):
        if self.que_one.is_empty():
            print('the queue is empty')
            return
        while self.que_one.front != self.que_one.rear:
            self.que_two.en_que(self.que_one.de_que())
        temp = self.que_one.de_que()
        self.temp_que = self.que_one
        self.que_one = self.que_two
        self.que_two = self.temp_que
        return temp
    
    def top(self):
        if self.que_one.is_empty():
            return False
        else:
            return self.que_one.que_front()
        
    
st = Stack_costly_pop()
st.push(10)
st.push(11)
st.push(12)
st.push(14)
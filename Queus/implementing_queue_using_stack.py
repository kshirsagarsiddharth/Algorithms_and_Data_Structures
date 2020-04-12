# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 07:33:25 2020

@author: siddharth
"""


class de_que_costly_Queue:
    def __init__(self,capacity):
        self.stack_one = [None] * capacity
        self.stack_two = [None] * capacity
        
    def stack_enque(self,data):
        if len(self.stack_one) <= 0 or len(self.stack_two) <= 0:
            print('Both stacks are empty')
            return
        else:
            self.stack_one.append(data)
            print('stack_one is appended with {}'.format(data))
            
    def stack_deque(self):
        if len(self.stack_one) <= 0 or len(self.stack_two) <= 0:
            print('Both stacks are empty')
            return
        if len(self.stack_two) <= 0:
            while len(self.stack_one) != 0:
                self.stack_two.append(self.stack_one[-1])
                self.stack_one.pop()
        temp = self.stack_two[-1]
        self.stack_two.pop()
        
        if len(self.stack_one)<= 0:
            while len(self.stack_two) != 0:
                self.stack_one.append(self.stack_two[-1])
                self.stack_two.pop()
        print('the queue is dequed with {}'.format(temp))
        return temp 
    
    
        
class en_que_costly_Queue:
    def __init__(self,capacity):
        self.stack_one = [None] * capacity
        self.stack_two = [None] * capacity
        
    def stack_enque(self,data):
        
        if len(self.stack_one) <= 0 or len(self.stack_two) <= 0:
            print('Both stacks are empty')
            return
    
    
        
        while len(self.stack_one) != 0:
            self.stack_two.append(self.stack_one[-1])
            self.stack_one.pop()
        
        self.stack_one.append(data)
        print('the data appended is {}'.format(data))
        
        while(len(self.stack_two) != 0):
            self.stack_one.append(self.stack_two[-1])
            self.stack_two.pop()

    def stack_deque(self):
        if len(self.stack_one) <= 0 or len(self.stack_two) <= 0:
            print('Both stacks are empty')
            return
        x = self.stack_one[-1]
        self.stack_one.pop()
        return x
 
    
            
dqc = de_que_costly_Queue(10)

dqc.stack_enque(10)
dqc.stack_enque(11)
dqc.stack_enque(12)

dqc.stack_deque()

enc = en_que_costly_Queue(10)

enc.stack_enque(10)          

           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
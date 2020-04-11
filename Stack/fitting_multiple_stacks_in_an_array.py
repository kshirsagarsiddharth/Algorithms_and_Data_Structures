# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 04:14:17 2020

@author: siddharth
"""

'''Algorithm for fitting three stacks
Top1 = size of first stack
Top2 = size of the second stack
Top3 = size of third stack

Pushing:
    For pushing onto the first stack
    we need to see if adding new element, into first stack causes it to bump,
    with third stack if so try to shift the third stack upwards.
    Insert new element at (start1 + top1)
    
    For pushing onto second stack
    we need to see if adding new element causes it to bump into the
    third stack .if so try to shift the third stack downwards .
    insert new element at start2 - top2
    
    For pushing onto the third stack see if it bumps onto the
    third stack.
    if so try to shift the third stack downwards, and try pushing again
    insert new element at start3 + top3

Popping: For Popping, There is no need to shift just decrement the 
         value form the appropriate stack.
'''

'''
Fittimg m stacks in n size array

let us assume that the array indexes are from 1 to n. to implement m stacks in one array
we divide the array into m parts the size of each port is n/m 

From the representation of the stack we can observe that stack is starting at index 1
(starting index is stored in base 1) second stack is starting at index n/m(starting index 
of the second stack is stored in base[2]). Third stack is starting at the index 2n/m
 and so on.
Base array stores the starting index of the array

Top array stores the top indexes of each stack

Top[i] for 1<= i <= m will point to the topmost element of stack i

if base[i] == top[i] then we can say that the stack is empty

if top[i] == base[i + 1] then we can say that the stack is full

initally base[i] = top[i] = n/m(i - 1) for 1 <= i <= m

the i'th stack grows from base[i] + 1 to base[i + 1] 

'''
# implementing two stacks in an array
class TwoStacks:
    
    def __init__(self,n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = self.size
        
    # pushing an element into stack1
    
    def push1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.array[self.top1] = x
        else:
            print('stack overflow')
            exit('dates')
            
    def push2(self,x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.array[self.top2] = x
        else:
            print('stack overflow')
            exit('dates2')
            
            
    def pop1(self):
        if self.top1 >= 0:
            x = self.array[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print('stack underflow')
            exit('pops')
            
    def pop2(self):
        if self.top2 < self.size:
            x = self.array[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print('stack underflow')
            exit('dates 2')
'''
top[] : this is of size k and stores indexes of top elements in all stacks.

next[] : this is of size n and stores indexes of next item for items in an array.
here arr[] is the actual array that stores k stacks .
Togther with the k stacks a stack of free slots in arr[] is also maintained. The top of this stack is 
stores in a variable free

All entries in top[] are initialized with -1 to indicate all the stacks are initially empty. all entries in next[i] arfe initialized with i + 1
because all slots are free initially and are pointing to next slot.
Top of the free stack free is initialized to 0
'''      
        
class KStacks:
    def __init__(self,k,n):
        self.k = k # number of stacks
        self.n = n # total size of the array holding k stacks
        
        # array which stores k stacks 
        self.array = [None] * self.n
        # all stacks are empty to begin with 
        # -1 in the array indicates that the stack is empty
        
        self.top = [-1] * self.k
        
        # top of the free stack
        # or tells how many elements are
        # free in the stack
        self.free = 0
        
        # points to the next element in either
        # onke of the k stacks of the free stack
        
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1 # because last element in the next array cannot
        # point to anything hence we initialize it to point to one.
        
        # check wether a given stack is empty
        # this function takes the stack number as
        # input
        def is_empty(self,stack_number):
            return self.top[stack_number] == -1
        
        # this helper function checks wether there are any 
        # spaces left to push new elements onto the stack 
        def is_full(self):
            return self.free == -1
        
        # function to push element on given stack_number
        def push(self,item,stack_number):
            if self.is_full():
                print('there is a stack overflow')
                return
            # get the first free position to insert at
            insert_at = self.free
            
            self.free = self.next[self.free]
            # insert the item at the free position
            # we obtained above
            self.array[insert_at] = item
            
            # adjust the next to point to the
            # old top of the stack element
            
            self.next[insert_at] = self.top[stack_number]
            
            # set the new top of the stack
            self.top[stack_number] = insert_at
            
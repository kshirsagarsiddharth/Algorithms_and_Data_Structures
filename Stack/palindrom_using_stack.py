# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:08:35 2020

@author: siddharth
"""

'''Algorithm
1) Traverse the list until we encounter X as input element

2) During the traveling push all the elements until X onto the
   stack

3) for the second half of the list, compare each elements content with
   the top of the stack. If they are the same pop the stack and go to the 
   next element in the input list.

4) continue the process until the stack is empty or the string is not a
   palindrom
'''



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



def palindrom_using_stack(str):
    st = Stack()
    palindrom = False
    
    for char in str:
        st.push(char)
    
    for char in str:
        if st.pop() == char:
            palindrom = True
        else:
            palindrom = False
    
    return palindrom


class CheckPalindrom:
    def palinderom_with_array(self,array):
        i = 0
        j = len(array) - 1
        while(j > i and array[j] == array[i]):
            i += 1
            j -= 1
        
        if i > j:
            return False
        else:
            return True
        


print(palindrom_using_stack('smadams'))
        
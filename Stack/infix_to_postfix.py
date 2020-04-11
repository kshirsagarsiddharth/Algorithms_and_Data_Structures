# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:14:52 2020

@author: siddharth
"""

'''Algorithm
1.scan the infix expression grom left to right
2.If the scanned character is a operand output it.
3.ELSE
    3.1 if the precidence of the scanned operator is greater than the 
    precidence of the operator in the stack (or the stack is empty or 
                                             the stack contains a '('),push it.
    3.2 else pop all the operators, from the stack which are
    greater than or equall to in precidence than that of the scanned operator.
    after doing that push scanned operator on the stack.
    (if you encounter a paranthesis while popping than stop there and push the 
     scanned operator in the stack).
4.if an scanned character is an '(', push it to the stack.
5.if the scanned character is an ')' pop the stack and output it untila '(' is
encounteres, and discard both paranthesis
6.repeat the steps 2-6 until infix expression is scanned
7.print the output
8.pop and output from the stack until it is not empty.
'''
# converting infix expression to postfix

class InfixToPostfix:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        # this array is used as a stack
        self.array = []
        # this is the output array
        self.output = []
        # this dictonary is for precidence setting
        self.precidence = {'+':1,'-':1,'*':2,'/':2,'^':3}
        
    # check if the stack is empty
    def is_empty(self):
        return True if self.top == -1 else False
    
    # return the value of top of the stack
    # to make a note top element of stack is end element of an array
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.array.pop()
        else:
            return False
        
   
    
    def push(self,operator):
        self.top = self.top + 1
        self.array.append(operator)
    
    # a utility function which checks wether the input is a operand
    def is_operand(self,character):
        return character.isalpha()
    
    # check the precidence of operators is strictly 
    #less than the top of the stack
    def not_greater(self,i):
        try:
            a = self.precidence[i]
            b = self.precidence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    # main function that converts infix expression into postfix expression
    
    def infix_to_postfix(self,expression):
        
        # iterate over the whole expression
        for i in expression:
            # if the character is operand add it to
            # the output
            if self.is_operand(i):
                self.output.append(i)
                 # if '(' is the character push it onto the stac
            elif i == '(':
                self.push(i)
                # if the scanned character is ')' pop and
                # and output from the stack until '(' is found
            elif i == ')':
                while ((not self.is_empty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                    # in this case while travelling we should atleast 
                    # get a ( if it is not there and after removing all the 
                    # paranthesis if the stack is not empty then throw a error
                if (not self.is_empty() and self.peek() != '('):
                    return -1
                else:
                    self.pop() # this is to pop the remaining '('
            # an operator is encountered 
            # and if the precidence of the operator is less than top of the stack
            # than we pop the element with highest presidence to the output
            else:
                while(not self.is_empty() and self.not_greater(i)):
                    self.output.append(self.pop())
                self.push(i) # but if the precidence of the operator is greater than the 
                # top of the stack than the while loop is not executed and the operator 
                # is simply pushed onto the stack
        # with this loop we pop all the remaining operators in the stack to the 
        # output array
        while not self.is_empty():
            self.output.append(self.pop())

        print("".join(self.output))                
                        
        
exp = "a + b * ( c ^ d - e ) ^ ( f + g * h ) - i".split()
st = InfixToPostfix(100)
st.infix_to_postfix(exp)              
           
       
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
            
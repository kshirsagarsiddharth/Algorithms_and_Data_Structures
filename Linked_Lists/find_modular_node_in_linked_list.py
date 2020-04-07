# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:58:03 2020

@author: siddharth
"""
'''
    1)initialize two counters i and j both to 1 and a pointer sqrtn to NuLL to traverse till the required position is reached
    
    2) start traversing the list using head node until last node is reached
    
    3) while traversing check if value of j is equal to sqrt(i). If the values are equal
    Increment both i and j and sqrtn to point sqrtn.next otherwise increment only i
    4) now when we will reach the last node of list i will contain value of n, j will contain value of sqrt(i) 
    and sqrtn will point to node of jth position
    '''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_from_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    
    def print_linked_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def modular_node(self,k):
        
        current = self.head
        modular_node = None
        i = 1
        if (k < 0 ):
            return None
       
        while(current is not None):
            if (i % k == 0):
                modular_node = current
            i+=1
            current = current.next
        
        return modular_node.data
    def fractional_node(self,k):
       current = self.head
       fractional_node = None
       i = 1
       if (k < 0 or current == None):
           return None
       while (current is not None):
           if (i % k == 0):
               if (fractional_node is None):
                   fractional_node = self.head
               else:
                   fractional_node = fractional_node.next
           i = i + 1
           current = current.next
       return fractional_node.data        
    
    
    def squareroot_node(self):
        sqrtn = None
        i = 1
        j = 1
        current = self.head
        while(current is not None):
            if (i == j ** 2):
                if sqrtn is None:
                    sqrtn = self.head
                else:
                    sqrtn = sqrtn.next
                j += 1
            i += 1
            current = current.next
        return sqrtn.data
    
       
            
ll = LinkedList()

for i in reversed(range(1,10)):
    ll.insert_from_beginning(i) 

print(ll.squareroot_node())

        
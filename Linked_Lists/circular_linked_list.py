# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 04:45:14 2020

@author: siddharth
"""

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        self.length = 0
        self.head = None
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next is not None
    
    def list_length(self):
        if self.head is None:
            return 0
        else:
            count = 1
            next_node = self.head.get_next()
            while next_node != self.head:
                count += 1
                next_node = next_node.get_next()
            return count
        
    def print_linked_list(self):
        if self.head is None:
            print('The linked list does not exist')
        else:
            # we are writhin this initial statements because if the circular linked list has only one node it will start with head and end with 
            #head
            current = self.head
            print(current.get_data())
            current = current.get_next()
            while current != self.head:
                print(current.get_data())
                current = current.get_next()
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.set_next(new_node) # this is a circular linked list hence when we add a new node what we do is
            # we set the same node as its next node i.e the pointer of the head node points to itself
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            # by performing this looping we get last node now we need to insert new node after this node
            current.set_next(new_node)
            new_node.set_next(self.head)
        self.length += 1
        
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            new_node.set_next(self.head)
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
             new_node.set_next(self.head)
            current.set_next(new_node)
            self.head = new_node
        self.length += 1
                
    def delete_from_end(self):
        if self.head is None:
            raise ValueError('Linked list is not defined')
        else:
            current = self.head
            previous = None
            while current.get_next() != self.head:
                previous = current
                current = current.get_next()
            previous.set_next(self.head)
            current.set_next(None)
            self.length -= 1
    
    def delete_from_beginning(self):
        if self.head is None:
            raise ValueError('the list is empty')
        else:
            current = self.head
            next_node = current.get_next()
            while next_node.get_next() != self.head:
                next_node = next_node.get_next()
            next_node.set_next(current.get_next())
            self.head = current.get_next()
            current.set_next(None)
            self.length -= 1

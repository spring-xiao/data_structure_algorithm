# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:23:08 2020

@author: xiaoxiang
"""

from linked_list import Node
from pyarray import Array

class linkedStack(object):
    '''
    链式栈
    '''
    
    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def __str__(self):
        
        if self.__head is None:
            output_str = '空栈'
        else:
            output_str = f'栈的长度为{self.__count}'
        
        return output_str
    
    __repr__ = __str__
    
    
    def push(self,data):
        
        node = Node(data)
        if self.__head is None:
            self.__head = node
        else:
            node.next_node = self.__head
            self.__head = node
        self.__count += 1
        
    def pop(self):
        
        if self.__head is None:
            print('空栈')
            return None
        
        else:
            node = self.__head
            self.__head = node.next_node
            self.__count -= 1
            return node.data
    
    @property
    def count(self):
        return self.__count
    
    
class arrayStack(object):
    '''
    顺序栈
    '''
    
    def __init__(self,capacity):
        self.__array = [None] *capacity
        self.__capacity = capacity
        self.__count = 0
        
    def __str__(self):
        
        if self.__count == 0:
            output = '空栈'
        else:
            output = f'栈的长度{self.__count}'
        return output    
    
    __repr__  = __str__
    
    def push(self,data):
        
        if self.__count >= self.__capacity:
            new_array = [None]*(self.__capacity * 2)
            for i in range(self.__capacity):
                new_array.insert(i,self.__array[i])
            
            self.__capacity = self.__capacity * 2
            self.__array = new_array
            
        self.__array.insert(self.__count,data)
        self.__count += 1
    
    def pop(self):
        
        if self.__count == 0:
            print("空栈")
            return None
        else:
            self.__count -= 1
            data = self.__array[self.__count]
            #self.__array.pop(self.__count)
            return data


if __name__ == '__main__':
    
    linked_stack = linkedStack()
    for i in range(10):
        linked_stack.push(i)
    
    linked_stack.pop()

    array_stack = arrayStack(10)
    for i in range(10):
        array_stack.push(i)

    for i in range(10,20):
        array_stack.push(i)




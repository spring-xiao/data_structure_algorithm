# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:35:11 2020

@author: xiaoxiang
"""

from linked_list import Node

class linkedQueue(object):
    '''
    链式队列
    '''
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def __str__(self):
        if self.__head is None and self.__tail is None:
            output = '空队列'
        else:
            output = f'队列长度为{self.__count}'
        return output
    
    __repr__ = __str__
    
    def enqueue(self,value):
        
        node = Node(value)
        if self.__tail is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next_node = node
            self.__tail = node
        
        self.__count += 1
        
    def dequeue(self):
        
        if self.__head is None:
            print('空队列')
            return None
       
        data = self.__head.data
        node = self.__head
        self.__head = node.next_node
        if self.__head is None:
            self.__tail = None
        
        del(node)        
        self.__count -= 1

        return data
        
    
class arrayQueue(object):
    '''
    顺序队列
    '''

    def __init__(self,capacity):
        self.__head = 0
        self.__tail = 0
        self.__count = 0
        self.__capacity = capacity
        self.__array = [None] * capacity
        
    def __str__(self):
        if self.__head == self.__tail:
            output = '空队列'
        else:
            output = f'队列长度为{self.__count}'
        
        return output
    
    __repr__ = __str__
    
    def enqueue(self,value):
        if self.__tail == self.__capacity:
            if self.__head == 0:
                print('队列已满')
                return False
            
            for i in range(self.__head,self.__tail):
                self.__array[i-self.__head] = self.__array[i]
            
            self.__tail -= self.__head
            self.__head = 0

        self.__array.insert(self.__tail,value)
        self.__tail += 1
        self.__count += 1
    
        return True
    
    def dequeue(self):
        
        if self.__head == self.__tail:
            print("空队列")
            #self.__head = 0
            #self.__tail = 0
            return None
        data = self.__array[self.__head]
        self.__head += 1
        self.__count -= 1

        return data


class cycleArrayQueue(object):
    '''
    基于数组的循环队列
    '''
    
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__head = 0
        self.__tail = 0
        self.__array = [None] * capacity
    
    def enqueue(self,value):
        
        if (self.__tail + 1) % self.__capacity == self.__head:
            new_array = [None] * self.__capacity * 2
            i = 0
            while self.__head != self.__tail:
                new_array[i] = self.__array[self.__head]
                i += 1
                self.__head = (self.__head + 1) % self.__capacity
            
            self.__head = 0
            self.__tail = i 
            self.__capacity *= 2
            self.__array = new_array
            
        self.__array[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__capacity


    def dequeue(self):
        
        if self.__head == self.__tail:
            print('空队列')
            return None
        
        data = self.__array[self.__head]
        self.__head = (self.__head + 1) % self.__capacity
        return data
            
    
if __name__ == '__main__':
    
    linked_queue = linkedQueue()
    for i in range(10):
        linked_queue.enqueue(i)
        
    linked_queue.dequeue()


    array_queue = arrayQueue(20)
    for i in range(10):
        array_queue.enqueue(i)
    
    array_queue.dequeue()


    cycle_array_queue = cycleArrayQueue(10)
    for i in range(15):
        cycle_array_queue.enqueue(i)
        
    cycle_array_queue.dequeue()



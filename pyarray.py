
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:23:57 2020

@author: xiaoxiang
"""

class Array():
    '''
    数组结构
    '''
    
    def __init__(self,capacity):
        self.__data = [None] * capacity
        self.__capacity = capacity
        self.__count = 0
    
    def __str__(self):
        output = ', '.join([str(i) for i in self.__data[0:self.__count]])
        output = '[' + output +']'
        return  output
    
    __repr__ = __str__
    
    def __len__(self):
        return self.__count
      
    def __getitem__(self,index):
                
        if index < 0 or index >= self.__count:
            raise ValueError(f"索引位置非法,要求index>=0 且 index<{self.__count}")
            
        else:
           return self.__data[index]
    
    def __setitem__(self,index,value):
        
        if index < 0 or index >= self.__count:
            raise ValueError(f"索引位置非法,要求index>=0 且 index<{self.__count}")
        else:
            self.__data[index] = value
            
    def find(self,index):
        
        res = self.__getitem__(index)
        return res
    
    def insert(self,index,value):
        
        if self.__count == self.__capacity:
            raise ValueError("数组已满,无法插入")
            
        if index < 0 or index > self.__count:
            raise ValueError("插入位置非法,要求index>=0 且 index<={self.__count}")
        
        i = self.__count
        while i > index:
            self.__data[i] = self.__data[i-1]
            i -= 1
        
        self.__data[index] = value
        self.__count += 1
        
    def insertFirst(self,value):
        self.insert(0,value)
    
    def insertTail(self,value):
        self.insert(self.__count,value)
    
    def delete(self,index):
        
        if index < 0 or index >= self.__count:
            raise ValueError("插入位置非法,要求index>=0 且 index<{self.__count}")
                
        data = self.__data[index]   
        for i in range(index+1,self.__count):
            self.__data[i-1] = self.__data[i]
            
        self.__count -= 1
        return data
    
    @property
    def count(self):
        return self.__count
 
    @property
    def capacity(self):
        return self.__capacity


if __name__ == '__main__':
    
   array = Array(20)
   
   array.insert(0,1)
   array.insert(1,2)
   array.insert(2,3)
   array.insert(0,2)
   
   array.delete(1)
   
   array[1] = 10
   array.insertFirst(20)
   array.insertTail(30)
   
   for i in range(array.count):
       print(array[i])

   array[10] = 10



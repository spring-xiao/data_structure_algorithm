# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:23:39 2020

@author: xiaoxiang
"""

from pyarray import Array

def bubble_sort(array):
    '''
    冒泡排序
    '''
    length = len(array)
    for i in range(length):
        flag_change = False
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                val = array[j]
                array[j] = array[j + 1]
                array[j + 1] = val
                flag_change = True
        if not flag_change:
            break
    
    return array
    
 
if __name__ == '__main__':
    
    array1 = [2,5,9,4,1,2,3,6]
    
    array2 = Array(20)
    for i in array1:
        array2.insertTail(i)
    
    bubble_sort(array1)
    bubble_sort(array2)













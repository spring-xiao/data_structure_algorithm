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
            if array[j] > array[j+1]:
                val = array[j]
                array[j] = array[j+1]
                array[j+1] = val
                flag_change = True
        if not flag_change:
            break
    
    return array
    

def insert_sort(array):
    '''
    插入排序
    '''
    length = len(array)
    for i in range(1,length):
        val = array[i]
        for j in range(i-1,-1,-1):
            if array[j] > val:
                array[j+1] = array[j]
            else:
                break
            
        if j == 0 and array[j] > val:
            array[0] = val
        else:
            array[j+1] = val    
            
    return array        
    
            
def select_sort(array):
    '''
    选择排序
    '''
    length = len(array)
    for i in range(length):
        min_val = array[i]
        min_index = i 
        for j in range(i+1,length):
            if min_val > array[j]:
                min_val = array[j]
                min_index = j
        val = array[i]
        array[i] = min_val
        array[min_index] = val
     
    return array


def merge_sort(array):
    '''
    归并排序
    '''
    def merge_sort_r(array,start,end):
        
        if start >= end:
            return
        mid = int((end + start)/2)
        merge_sort_r(array,start,mid)
        merge_sort_r(array,mid+1,end)
        
        i = start
        j = mid + 1
        k = 0
        tmp = Array(end - start + 1) if isinstance(array,Array) else []
        while i <= mid and j <= end:
            if array[i] <= array[j]:
                tmp.insert(k,array[i])
                i += 1
            else:
                tmp.insert(k,array[j])
                j += 1
            k += 1
        
        if i <= mid:
            while i <= mid:
                tmp.insert(k,array[i])
                k += 1
                i += 1
            
        if j <= end:
            while j <= end:
                tmp.insert(k,array[j])
                k += 1
                j += 1
        
        for i in range(end - start + 1):
            array[start + i] = tmp[i]
        
    length = len(array)
    merge_sort_r(array,0,length-1)
    
    return array
    
def quick_sort(array):
    '''
    快速排序
    '''
    def quick_sort_r(array,start,end):
        
        if start >= end:
            return
        
        pivot = array[end]
        i = start
        j = start
        
        while j < end:
            if array[j] < pivot:
                val = array[i]
                array[i] = array[j]
                array[j] = val
                i += 1
            j += 1
         
        val = array[i]
        array[i] = array[end]
        array[end] = val
        
        quick_sort_r(array,start,i-1)
        quick_sort_r(array,j,end)
    
    length = len(array)
    quick_sort_r(array,0,length-1)
    return array

def bucket_sort(array):
    pass

def count_sort(array):
    pass



if __name__ == '__main__':
    
    array1 = [2,5,9,4,1,2,3,6]
    
    array2 = Array(20)
    for i in array1:
        array2.insertTail(i)
     
    bubble_sort(array1)
    bubble_sort(array2)

    insert_sort(array1)
    insert_sort(array2)

    select_sort(array1)
    select_sort(array2)
    
    merge_sort(array1)
    merge_sort(array2)

    array1 = [2,5,6,2,4,8,9,5,20,12,4,5,12,10]
    quick_sort(array1)
    quick_sort(array2)
    





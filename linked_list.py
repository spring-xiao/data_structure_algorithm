# -*- coding: utf-8 -*-

"""
Created on Fri Sep 11 10:14:18 2020

@author: xiaoxiang
"""

'''
单链表反转
链表中环的检测
两个有序的链表合并
删除链表倒数第 n 个结点
求链表的中间结点
'''

class Node():
    '''
    
    '''
    def __init__(self,data,next_node = None):
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,data):
        self.__data = data
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self,next_node):
        self.__next_node = next_node


class linkedList():
    
    '''
    链表数据结构
    '''
    def __init__(self,head = None):
        self.__head = head
        self.__count = 0
    
    def __str__(self):
        
        if self.__head is None:
            return '空链表'
        else:
            return '链表长度为{}'.format(self.__count)
            
    __repr__ = __str__
    
    
    def find_by_value(self,value):
        
        node = self.__head
        while node is not None:
            if node.data == value:
                break
            node = node.next_node
        
        return node
            
    
    def find_by_index(self,index):
        
        if index < 0 or index >= self.__count:
            print("索引非法或超过链表长度")
            return None
            
        pos = 0
        node = self.__head
        while node is not None:
            if pos == index:
                break
            node = node.next_node
            pos += 1
        
        return node
        
    
    def insert_head(self,value):
        
        node = self.create_node(value) 
        
        node.next_node = self.__head
        self.__head = node
        self.__count += 1
        return True
    
    def insert_tail(self,value):
        
        node_new = self.create_node(value) 
        node_tail = self.search_tail_node()
        if node_tail is None:
            self.__head = node_new
        else:
            node_new.next_node = node_tail.next_node
            node_tail.next_node = node_new
        self.__count += 1
    
        return True
            
            
    def insert_before(self,node,value):
        
        if node is None:
            print("无法在空节点前插入")
            return False
    
        if self.__head is None:
            print("链表为空,无法插入指定节点前")
            return False
        
        if node == self.__head:
            self.insert_head(value)
            return True
        
        node_prev = self.search_node_prev(node)
        if node_prev is None:
            return False
        
        node_new = Node(value) 
        node_new.next_node = node_prev.next_node
        node_prev.next_node = node_new
        self.__count += 1
        return True
        
    def insert_after(self,node,value):
        
        if node is None:
            print("无法在空节点后插入")
            return False
            
        if self.__head is None:
            print("链表为空,无法插入指定节点后")
            return False        
       
        is_exist = self.is_exist_node(node)
        if not is_exist:
            print("节点不在于链表中")
            return False
        
        node_new = Node(value) 
        node_new.next_node = node.next_node
        node.next_node = node_new
        self.__count += 1
        return True

    def delete_by_node(self,node):
        if self.__head is None:
            print("空链表")
            return False
        if self.__head == node:
            self.__head = node.next_node
            self.__count -= 1
            return True
        
        node_prev = self.search_node_prev(node)
        if node_prev is not None:
            node_prev.next_node = node.next_node
            self.__count -= 1
            return True
            
        return False
        
    
    def delete_by_value(self,value):
        if self.__head is None:
            print("空链表")
            return False
        if self.__head.data == value:
            self.__head = self.__head.next_node
            self.__count -= 1
            return True
        
        node_prev = self.search_node_prev_by_value(value)
        if node_prev is not None:
            node_prev.next_node = node_prev.next_node.next_node
            self.__count -= 1
            return True
        
        return False
        
    
    def search_node_prev_by_value(self,value):
        
        if self.__head is None:
            print("空链表")
            return None
        elif self.__head.data == value:
            print("节点为头节点,无前向节点")
            return None
        else:
            node_prev = self.__head
            while node_prev.next_node is not None:
                if node_prev.next_node.data == value:
                    return node_prev
                
                node_prev = node_prev.next_node
            
            print("链表中不存在该值")
            return None
         
    
    def search_node_prev(self,node):
        
        if self.__head is None:
            print("空链表")
            return None
        elif self.__head == node:
            print("节点为头节点,无前向节点")
            return None
        else:
            node_prev = self.__head
            while node_prev.next_node != node:
                
                if node_prev.next_node is None:
                    print("节点不存在于链表中")
                    return None
                node_prev = node_prev.next_node
                
            return node_prev
        
    
    def search_tail_node(self):
        
        if self.__head is None:
            print("空链表")
            return None
        else:
            node_tail = self.__head
            while node_tail.next_node is not None:
                node_tail = node_tail.next_node
                
            return node_tail
        
    def is_exist_node(self,node):
        
        if self.__head is None:
            return False
        else:
            node_point = self.__head
            while node_point != node:
                if node_point.next_node is None:
                    return False
                node_point = node_point.next_node
            
            return True
        
    def create_node(self,value,next_node = None):
        
        node = Node(value,next_node)
        return node
    
    
    def delete_last_n_node(self,n):
        
        if self.__head is None:
            print('空链表')
            return False
        
        self.reverse()
        node_prev = self.find_by_index(n-1)
        self.delete_by_node(node_prev)
        self.reverse()
        
        return True
        
    def has_cycle(self):
        '''
        
        '''
        pass
    
    
    def merge(self,linked_list):
        '''
        两个有序列表合并
        '''
        
        head1 = self.head
        head2 = linked_list.head
        
        if head1 is None and head2 is None:
            print('两个空链表')
            return False
        
        if head1 is None and head2 is not None:
            self.__head = linked_list.head
            self.__count = linked_list.count
            return True
        
        if head1 is not None and head2 is None:
            return True
        
        
        if head1.data <= head2.data:
            head_new = head1
            head1 = head1.next_node
            
        else:
            self.__head = head2
            head_new = head2
            head2 = head2.next_node
            
        while head1 is not None and head2 is not None:
            if head1.data <= head2.data:
                head_new.next_node = head1
                head_new = head1
                head1 = head1.next_node
                
            else:
                head_new.next_node = head2
                head_new = head2
                head2 = head2.next_node
            
        if head1 is not None:
            head_new.next_node = head1
        
        if head2 is not None:
            head_new.next_node = head2
            
        self.__count += linked_list.__count
        
        return True
        
    
    def reverse(self):
        '''
        链表反转
        '''
        if self.__head is None:
            print('空链表')
            return False
        
        node_first = self.__head
        node_tmp = self.__head.next_node
        while node_tmp is not None:
            node_first.next_node = node_tmp.next_node
            node_tmp.next_node =self.__head
            self.__head = node_tmp
            node_tmp = node_first.next_node
            
        return True
    
    def search_mid_node(self):
        '''
        求链表的中间结点
        '''
        if self.__head is None:
            return None
        
        if self.__head.next_node is None:
            return self.__head
        
        fast_point = self.__head
        slow_point = self.__head
        while slow_point.next_node is not None and slow_point.next_node.next_node is not None:
            fast_point = fast_point.next_node
            slow_point = slow_point.next_node.next_node
        
        return fast_point
        
        
    @property
    def head(self):
        return self.__head
                
    @property
    def count(self):
        return self.__count
    
            
if __name__ == '__main__':
    
    linked_list = linkedList()
        
    for i in range(10):
        linked_list.insert_tail(i)
    
    linked_list.insert_head(0)    
    linked_list.insert_head(1)
    linked_list.insert_head(2)
    linked_list.insert_tail(9)
    linked_list.insert_tail(10)

    node4 = linked_list.find_by_index(3)
    node9 = linked_list.find_by_index(8)
    
    linked_list.insert_after(node4,44)
    linked_list.insert_after(node9,99)
     
    linked_list.delete_by_value(0)
    linked_list.delete_by_value(9)
    linked_list.delete_by_node(linked_list.find_by_index(4))
    linked_list.delete_by_node(linked_list.find_by_value(44))
    linked_list.delete_by_node(linked_list.find_by_value(1))
    linked_list.delete_by_node(linked_list.find_by_value(99))

    linked_list.search_mid_node()
    linked_list.reverse()
    linked_list.delete_last_n_node(5)
    node = linked_list.head
    while node is not None:
        print(node.data)
        node = node.next_node

    #-------------------------
    linked_list1 = linkedList()
    linked_list2 = linkedList()
    linked_list3 = linkedList()

    for i in range(20):
        if i%2 == 0:
            linked_list1.insert_tail(i)
        else:
            linked_list2.insert_tail(i)

    linked_list1.merge(linked_list3)
    node = linked_list1.head
    while node is not None:
        print(node.data)
        node = node.next_node
        
    
    node = linked_list2.head
    while node is not None:
        print(node.data)
        node = node.next_node
    
    linked_list3.merge(linked_list2)
    node = linked_list3.head
    while node is not None:
        print(node.data)
        node = node.next_node
     

        

  


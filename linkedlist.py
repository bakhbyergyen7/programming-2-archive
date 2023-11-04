#linkedlist.py

from node import Node

class LinkedList:

    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self,index,entry):
        #Validate index
        #check for index 0
        #check for inserting in middle
        #check for inserting at end
        n = Node(entry)
        if index<0 or index>self._length:
            raise IndexError("Enter a valid index")
        elif  0<=index<=self._index:
            if index ==0:
                n.next = self._front
                self._front = n
                self._length+=1
            elif index == self._length:
                back = self._front
                for i in range(self._length-1):
                    back = back.next
                back.next = n
                self._length+=1
        else:
            i = 0
            jumper = self._front
            while i!=index-1:
                jumper = jumper.next
                i+=1
                var = jumper.next
                jumper.next = n
                n.next = var
                self._length+=1

    def remove(self, index):
        #validate index
        #remove item at index
        pass
    def get_entry(self,index):
        #define, raise error
        #if valid return value at
        #index
        jumper =self._front
        if index < self._length and index >= 0:
            jumper = jumper.next
            return jumper.entry
        else:
            raise IndexError('Failed!')
    def _get_node(self,index):
        #if index valid, return
        #node at the index
        pass
    def length(self):
        #returns length
        pass
#Author: Bakhbyergyen Yerjan | 9/28/2022 | Modified time 2:43PM

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def length(self):
        return self._length
        
    def insert(self,index,entry):
        n = Node(entry)
        if index < 0 or index > self.length():
            raise IndexError("Please enter a valid index")

        elif index == 0:
            n.next = self._front
            self._front = n

        elif index == -1:
            back = self._front
            for i in range(self.length()-1):
                back = back.next
            back.next = n
        else:
            i = 0
            prev_node = self._front
            while i != index-1:
                prev_node = prev_node.next
                i+=1
                var = prev_node.next
                prev_node.next = n
                n.next = var


    def remove(self,index):
        if index<0 or index >= self.length():
            raise IndexError("Please enter a valid index")
        elif index == 0:
            head = self._front
            self._front = self._front.next
            del head
        else:
            i = 0
            prev_node = self._front
            while i != index-1:
                prev_node = prev_node.next
                i+=1
            target = prev_node.next
            after = target.next
            del target
            prev_node.next = after

    def get_entry(self,index):
        jumper = self._front
        if index>=0 and index < self.length():
            i = 0
            while i <= index-1:
                jumper = jumper.next
                i+=1
        else:
            raise RuntimeError("Invalid Index!")

        return jumper.entry
    
    def set_entry(self,index,entry):
        #Sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same.
        target = self._front
        if index ==0:
            target.entry = entry
        if index<self.length() and index>0:
            i = 0
            while i < index-1:
                target= target.next
                i+=1
            target.entry = entry
        else: 
            raise RuntimeError("Invalid Index!")

    def clear(self):
        self._front = None
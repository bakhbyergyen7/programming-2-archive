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
        if index < 0 or index > self._length:
            raise IndexError("Please enter a valid index")
        #Inserting to empty list
        elif self._front == None:
            self._front = n
            self._length += 1
        #Inserting at Front
        elif index == 0:
            temp = self._front
            self._front = n
            self._front.next = temp
            self._length += 1
        #Inserting at Back
        elif index == self.length():
            jumper = self._front
            for i in range(self.length()-1):
                print(jumper.entry)
                jumper = jumper.next
            jumper.next = n
            self._length += 1
        # inserting in the middle
        else:
            i = 0
            prev_node = self._front
            while i != index-1:
                prev_node = prev_node.next
                i+=1
            var = prev_node.next
            prev_node.next = n
            n.next = var
            self._length += 1
        



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
        self._length -= 1

    def get_entry(self,index):
        if index < 0 or index >= self._length:
            raise IndexError("Invalid Index")
        jumper = self._front
        for i in range(0,index):
            jumper = jumper.next
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
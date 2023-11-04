# stack.py

from node import Node


class Stack:
    def __init__(self):
        self._top = None

    def push(self,entry):
        # create a node with the entry
        # put it on the top
        new = Node(entry)
        new.next = self._top
        self._top = new

    def is_empty(self):
        #return True if empty
        #or False otherwise
        return self._top == None


    def pop(self):
        #remove the top-most node
        #return the value in the node
        #raise RuntimeError if you can't pop
        if self.is_empty():
            raise RuntimeError("Empty Stack")
        else:
            top = self._top
            self._top = self._top.next
        return top
    
    

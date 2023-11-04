# stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def push(self,entry):
        new = Node(entry)
        new.next = self._top
        self._top = new

    def is_empty(self):
        return self._top == None

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Empty Stack")
        else:
            top = self._top
            self._top = self._top.next
        return top.entry
    
    

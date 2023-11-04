#queue.py

from node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
    def enqueue(self,entry):
        new = Node(entry)
        if self._front == None:
            self._back = new
            self._front = self._back
        else:
            self._back.next = new
            self._back = new
    def is_empty(self):
        return self._front == None
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Empty Queue")
        else:
            front = self._front
            self._front = self._front.next
            return front.entry
    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        else:
            return self._front.entry
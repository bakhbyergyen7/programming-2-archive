#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #Keep the "heap" complete
        self._heap.append(entry)
        self._upheap(len(self.heap)-1)

    def _upheap(self, index):
        """Upheaps value at given index
        to the correct position"""
        #Write a recursive definition
        if self._index == 0:
            return
        elif self._heap[]

    def _left_child(self, index):
        return 2*index+1
    def _right_child(self, index):
        return 2*index+2
    def _downheap(self, index):
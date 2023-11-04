#maxheap.py

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self._upheap(len(self.heap) - 1)

    def add(self, entry):
        self.heap.append(entry)
        self._upheap(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    def remove(self):
        if len(self.heap) > 2:
            self._swap(1,len(self.heap)-1)
            max = self.heap.remove()
            self._downheap(1)
        elif len(self.heap) == 2:
            max = self.heap.remove()
        else:
            max = False
        return max
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _upheap(self, index):
        """Upheaps value at given index
        to the correct position"""
        #Write a recursive definition
        parent = index//2
        if index <= 1:
            return
        elif self._heap[index] > self._heap[parent]:
            self._swap(index, parent)
            self._upheap(parent)


    def _downheap(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != right:
            self._swap(index, largest)
            self._downheap(largest)
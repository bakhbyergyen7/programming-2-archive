#binarysearchtree.py
from bnode import BNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search(self,key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        # Base 1: cur_node = None, raise an exception
        # Base 2: cur_node contains object matching key, 
        #           return the entry
        # Recursive case: Decide to go LST or RST by comparing
        #                 entry to the key
        if cur_node == None:
            raise RuntimeError("Doesn't exist")
        elif cur_node.entry == key:
            return cur_node.entry
        elif cur_node.entry < key:
            return self._rec_search(key, cur_node.right)
        elif cur_node.entry > key:
            return self._rec_search(key, cur_node.left)

    def add(self, entry):
        if self._root == None:
            self._root = BNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        if cur_node.entry < entry:
            if cur_node.right == None:
                cur_node.right = BNode(entry)
            else:
                return self._rec_add(entry, cur_node.right)
        elif cur_node.entry > entry:
            if cur_node.left == None:
                cur_node.left = BNode(entry)
            else:
                return self._rec_add(entry, cur_node.left)
        else:
            raise RuntimeError('Duplicate entry cannot be added!')

# In
    def traverse_in(self):
        self._rec_in(self._root)
    
    def _rec_in(self, cur_node):
        if cur_node != None:
            self._rec_in(cur_node.left)
            print(cur_node.entry)
            self._rec_in(cur_node.right)
# Pre
    def traverse_pre(self):
        self._rec_pre(self._root)

    def _rec_pre(self, cur_node):
        if cur_node != None:
            print(cur_node.entry)
            self._rec_pre(cur_node.left)
            self._rec_pre(cur_node.right)
# Post
    def traverse_post(self):
        self._rec_post(self._root)

    def _rec_post(self, cur_node):
        if cur_node != None:
            self._rec_post(cur_node.left)
            self._rec_post(cur_node.right)
            print(cur_node.entry)
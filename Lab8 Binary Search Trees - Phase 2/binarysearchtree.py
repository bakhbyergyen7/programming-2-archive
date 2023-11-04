#binarysearchtree.py
from bnode import BNode

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._copytree = None

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

# Cloning

    def _rec_copy(self, other_tree, cur_node):
        if cur_node != None:
            other_tree.add(cur_node.entry)
            self._rec_copy(other_tree, cur_node.left)
            self._rec_copy(other_tree, cur_node.right)

    def copy(self):
        newTree = BinarySearchTree()
        self._rec_copy(newTree, self._root)
        return newTree

# Remove
    def get_parent(self, key, cur_node):
        if self._root.entry == key:
            return self._root
        elif cur_node == None:
            raise RuntimeError("Went too far")
        elif cur_node.entry == key:
            raise RuntimeError("Passed parent node")
        elif cur_node.left.entry == key or cur_node.right.entry == key:
            return cur_node
        else:
            if cur_node.entry < key:
                return self.get_parent(key, cur_node.right)
            elif cur_node.entry > key:
                return self.get_parent(key, cur_node.left)

    def get_target(self, key, cur_node):
        if cur_node == None:
            raise RuntimeError("Doesn't exist")
        elif cur_node.entry == key:
            return cur_node
        elif cur_node.entry < key:
            return self._rec_search(key, cur_node.right)
        elif cur_node.entry > key:
            return self._rec_search(key, cur_node.left)

    def get_replacement(self, parent, child):
        if child == None:
            raise RuntimeError("Went too far")
        elif child.right != None:
            return self.get_replacement(child, child.right)
        else:
            parent.right = None
            return child

    def remove(self, key):
        target = self.get_target(key, self._root)
        if self._root.entry == key:
            if (target.right == None and target.left == None):
                self._root = None
            elif (target.right != None and target.left != None):
                replacement = self.get_replacement(target.left, target.left.right)
                replacement.left = target.left
                replacement.right = target.right
                self._root = replacement
            else:
                if target.right == None:
                    replacement = target.left
                else:
                    replacement = target.right
                self._root = replacement
        else:
            parent = self.get_parent(key, self._root)

            if (target.right == None and target.left == None):
                if parent.right.entry == key:
                    parent.right = None
                else:
                    parent.left = None
            elif (target.right != None and target.left != None):
                replacement = self.get_replacement(target.left, target.left.right)
                if parent.right.entry == key:
                    parent.right = replacement
                else:
                    parent.left = replacement
                replacement.left = target.left
                replacement.right = target.right
            else:
                if target.right == None:
                    replacement = target.left
                else:
                    replacement = target.right
                if parent.right.entry == key:
                    parent.right = replacement
                else:
                    parent.left = replacement
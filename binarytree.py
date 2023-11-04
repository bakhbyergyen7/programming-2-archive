#binarytree.py

from bnode import BNode

class BinaryTree:
    def _init_(self):
        self._root = None
    
    #Assume this works
    def add(self, entry):
        #Awesome, bugfree definition
        pass

    #public facing method
    def is_in(self, target):
        return self._rec_is_in(self,target, self._root)

    def _rec_is_in(self, target, cur_node):
        #recursive helper method
        #Base case: cur_node == None
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            is_in_LST = self._rec_is_in(target, cur_node.left)
            is_in_RST = self._rec_is_in(target, cur_node.right)
            return is_in_LST or is_in_RST

    def node_cont(self):
        return self._rec_node_count(self._root)
    def _rec_node_count(self, cur_node):
        if cur_node == None:
            return 0
        else:
            left = self._rec_node_count(cur_node.left)
            right = self._rec_node_count(cur_node.right)
            return 1+left+right

#mainbinary.py

from binarytree import BinaryTree

def mainbinary():
    my_tree = BinaryTree()
    my_tree.add("cat")
    my_tree.add("frogs")
    my_tree.add("lizard")
    my_tree.add("dinosaurs")

    if my_tree.is_in('frogs'):
        print("Ut oh! We got free frogs!")
    else:
        print("Phew! No frogs")
        
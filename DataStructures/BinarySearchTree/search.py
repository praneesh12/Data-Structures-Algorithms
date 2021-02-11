from BinarySearchTree import BinarySearchTree
from Node import Node
import display_tree

def search_bst(bst, val):
    """
    Search a value in a Binary Search Tree

    1. Access the root node
    2. Start binary search
            if val < root.val:
                search in left sub tree
            elif val > root.val:
                search in right sub tree 
    """
    root = bst.root
    if root is None:
        return "Value not found in Tree"

    # Base case val found at subTree
    if root.val == val:
        return True

    if val > root.val :
        if root.rightChild:
            return search_bst(root.rightChild, val)

    elif val < root.val:
        if root.leftChild:
            return search_bst(root.leftChild, val)



    

    

    



from Node import Node
from BinarySearchTree import BinarySearchTree

"""
    Implement a function findKthMax(root,k)
    which will take a BST and any number “k” as an input
    and return kth maximum number from that tree.
"""

"""
    We know the maximum value in a BST will be the right most leaf 
    So k-th Maximum will be, move k steps towwards the ancestors 
    using 
"""

def findMax(root):
    maxVal = None
    if root:
        if root.rightChild:
            return findMax(root.rightChild)
        else:
            maxVal = root.val
    return maxVal
    


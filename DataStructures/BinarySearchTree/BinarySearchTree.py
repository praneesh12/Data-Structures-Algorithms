from Node import Node
import display_tree 
import random
from collections import deque 

class BinarySearchTree:
    def __init__(self,val):
        self.root=Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False
    
    def delete(self, val):
        if self.root:
            self.root = self.root.delete(val)
        

def findMin(root):
    minVal = None
    if root:
        if root.leftChild:
            return findMin(root.leftChild)
        else:
            minVal = root.val
    print(minVal)
    return minVal

def findMax(root, stack):
    maxVal = None
    if root:
        stack.append(root)
        if root.rightChild:
            return findMax(root.rightChild,stack)
        else:
            maxVal = root.val
    print(maxVal)
    return maxVal



def findKthMax(root,k):

    if root is None:
        return root 
    
    left = findKthMax(root.leftChild,k)

    if left:
        return left 

    k -= 1

    if k==0:
        return root.val 

    return findKthMax(root.rightChild, k)



def kthSmallest(root,k):
    dequeList = deque(maxlen=k)
    while True:
        while root:
            dequeList.append(root)
            root = root.rightChild
        root = dequeList.pop()
        if k==1:
            return root.val
        k-=1
        root = root.leftChild









# bst = BinarySearchTree(50)
# for _ in range(3):
#     ele = random.randint(0, 100)
#     bst.insert(ele)
#     bst.insert(15)
#     display_tree.display(bst.root)
#     # Search for a random value 
# print(bst.search(15))


# BST = BinarySearchTree(6)
# BST.insert(3)
# BST.insert(2)
# BST.insert(4)
# BST.insert(-1)
# BST.insert(1)
# BST.insert(-2)
# BST.insert(8)
# BST.insert(7)

# print("before deletion:")
# display_tree.display(BST.root)

# BST.delete(2)
# print("after deletion:")
# display_tree.display(BST.root)

# print("*****Minimum Value in a BST*******")

# findMin(BST.root)

# print("*****Maximum Value in a BST*******")

# findMax(BST.root)


# for k in range(3,0,-1):
#     print(f"\n*****Find {k} highest Value in a BST*******")
#     print(findKthMax(BST.root,k))


# BST = BinarySearchTree(6)
# BST.insert(3)
# BST.insert(2)
# BST.insert(4)
# BST.insert(-1)
# BST.insert(1)
# BST.insert(-2)
# BST.insert(8)
# BST.insert(7)
# display_tree.display(BST.root)

# k=10
# print(f"{k}-th smallest element in BST: {kthSmallest(BST.root,k)}")



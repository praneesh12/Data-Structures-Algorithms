# 1 : In-order traversal method (left - root - right)
def inorderTraversal(root, stack):
    if root is None:
        return 
    
    if root:
        stack.append(root)
        root = inorderTraversal(root.leftChild, stack)
    
        root = stack.pop()
        print(root.val)

        root = inorderTraversal(root.rightChild, stack)
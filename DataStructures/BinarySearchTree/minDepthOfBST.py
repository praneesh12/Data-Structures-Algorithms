from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def minDepthBFS(root):
    
    queue = deque([root])
    minDepth = 0
    
    while queue:
        minDepth += 1
        for _ in range(len(queue)):
            root = queue.popleft()
            
            if (not root.left) and (not root.right):
                return minDepth
            # insert the children of current node in the queue
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    
    
    
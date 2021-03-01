from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                    current = current.next
                print()


def connectLevels(root):
    if not root:
        return None
    queue = deque([root])
    res = []
    while queue:
        prev = None
        level = []
        for _ in range(len(queue)):
            root = queue.popleft()
            level.append(root.val)
            if prev:
                prev.next = root
            prev = root 

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        res.append(level)
    return res
    




root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connectLevels(root)
print("Level order traversal using 'next' pointer: ")
root.print_level_order()
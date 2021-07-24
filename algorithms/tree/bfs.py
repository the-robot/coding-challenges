from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode):
    queue = deque([root])
    
    while queue:
        N = len(queue)
        
        for i in range(N):
            node = queue.popleft()
            print(node.val, end=" ")
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

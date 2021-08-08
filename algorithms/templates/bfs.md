# BFS

When I see BFS problem, I straight away think of deque (double ended queue) data structure. Because, when you traverse layer by layer,
you will need a data structure, that needs to pop first items, and at the same time, add new items from behind.

Basically it is a FIFO (first-in-first-out).

The template is fairly straight forward

```
a. create queue outside the iteration loop.
b. get current numbers of items (N) inside the queue and do iteration from (0 to N).
c. inside the iteration, get quueue item from left.
d. if you found child items, add it to the queue from behind.
```

Example solution for [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) problem.

```py
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        
        # a. add the root into queue
        queue = deque([root])
        result = []
        
        while queue:
            layer = []
            
            # b. get current number of items in queue and do iteration.
            N = len(queue)
            
            for i in range(N):
                # c. get queue item from left
                node = queue.popleft()
                
                # add the node to the current level
                layer.append(node.val)
                
                # d. insert the children of current node in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(layer)
        
        return result
```

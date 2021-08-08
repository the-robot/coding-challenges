[1. Backtracking](#1-backtracking)  
[2. BFS](#2-bfs)  

<br/>

# 1. Backtracking

```
a. Base Case
b. Recursion Block
c. Restore (pop) Block
```

So in general, backtracking should have those 3 blocks in a solution. For example, the solution below is for the [Combinations](https://leetcode.com/problems/combinations/) problem on leetcode.

```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.N = n
        self.K = k
        
        # store all possible combination elements
        self.nums = []
        for i in range(1, n + 1):
            self.nums.append(i)
        
        self.subsets = []

        # do backtracking        
        self.backtrack(0, [])
        
        return self.subsets
        
    def backtrack(self, index: int, subset: List[int]):
        # a. base case
        if len(subset) == self.K:
            self.subsets.append(subset[:])
            return
        
        # b. recursive calls
        #    as long as current index is not out of bound, we do backtrack
        if index < self.N:
            # do backtracking without current index
            self.backtrack(index + 1, subset)

            # do backtracking with current index
            subset.append(self.nums[index])
            self.backtrack(index + 1, subset)
            
            # c. popback the current index, so get back original subset
            subset.pop()
```

<br/>

# 2. BFS

When I see BFS problem, I straight away think of deque (double ended queue) data structure. Because, when you traverse layer by layer,
you will need a data structure, that needs to pop first items, and at the same time, add new items from behind.

Basically it is a FIFO (first-in-first-out).

The template is fairly straight forward

```
a. Create queue outside the while loop (loop until queue is empty).
b. Get current numbers of items (N) inside the queue and do iteration from (0 to N).
c. Inside the iteration, get queue item from left.
d. If you found child items, add it to the queue from behind.
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


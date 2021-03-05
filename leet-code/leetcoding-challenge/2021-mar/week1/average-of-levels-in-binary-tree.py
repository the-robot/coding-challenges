# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque
from typing import List

"""
Topic: Breadth First Search
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            levelSize = len(queue)
            total = 0.0
            
            for i in range(levelSize):
                node = queue.popleft()
                total += node.val
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            result.append(total / levelSize)

        return result

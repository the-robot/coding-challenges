# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.longest = 0
        
        self.dfs(root)
        
        return self.longest
        
    def dfs(self, root: TreeNode):
        if root is None:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        maximum = 1
        
        if root.left is None or root.left.val == root.val + 1:
            maximum = max(left + 1, maximum)
        
        if root.right is None or root.right.val == root.val + 1:
            maximum = max(right + 1, maximum)
        
        self.longest = max(self.longest, maximum)
        return maximum

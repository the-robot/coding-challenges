# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode):
    if root == None:
        return
    
    # traverse left
    inorder(root.left)
    
    # visit root
    print(root.val, end = " ")
    
    # traverse right
    inorder(root.right)
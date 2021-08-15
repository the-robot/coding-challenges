# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode):
    if root == None:
        return
    
    # visit root
    print(root.val, end = " ")
    
    # traverse left
    inorder(root.left)
    
    # traverse right
    inorder(root.right)


def preorder_iterative(root: TreeNode):
    stack = [root] # initalize stack

    while stack:
        current = stack.pop()

        print(current.val, end = " ")

        # Add right first, because in stack it is LIFO (Last In First Out)
        # because for pre-order, we want left first, so we add it later

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

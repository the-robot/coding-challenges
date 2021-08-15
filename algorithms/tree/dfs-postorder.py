# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root: TreeNode):
    if root == None:
        return
    
    # traverse left
    inorder(root.left)
    
    # traverse right
    inorder(root.right)
    
    # visit root
    print(root.val, end = " ")


def postorder_iterative(root: TreeNode):
    stack = [root]
    output = []
        
    while stack:
        current = stack.pop()

        output.append(current.val)

        # Add left first, because in stack it is LIFO (Last In First Out)
        # because for pre-order, we want right first, so we add it later

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    # reverse it
    output.reverse()
    
    # print values
    for v in reversed(output):
        print(v, end = " ")

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

def inorder_iterative(self, root: TreeNode):
        stack = []
        current = root
        
        while True:
            
            # reach the last most element of the current Node
            if current is not None:
                
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                
                current = current.left
            
            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif stack:
                current = stack.pop()
                
                print(current.val, end = " ")
                
                current = current.right
            
            else:
                break

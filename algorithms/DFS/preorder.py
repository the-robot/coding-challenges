from tree import TreeNode

def preorder(root: TreeNode):
    stack = [root]
    
    while stack:
        N = len(stack)
        
        for i in range(N):
            node = stack.pop()
            print(node.val, end=" ")
            
            # you have to add right first, because stack is LIFO (last in first out)
            # and for preorder, you want to traverse the left first
            
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

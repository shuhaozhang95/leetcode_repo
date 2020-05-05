# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ### Method 1: recursion
    def rootInRange(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val<=lower or val>=upper:
            return False
        if not self.rootInRange(node.left, lower, val):
            return False
        if not self.rootInRange(node.right, val, upper):
            return False
        return True

    def isValidBST01(self, root: TreeNode) -> bool:  
        return self.rootInRange(root)

    ### Method 2: Inorder traverse
    def isValidBST02(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
    
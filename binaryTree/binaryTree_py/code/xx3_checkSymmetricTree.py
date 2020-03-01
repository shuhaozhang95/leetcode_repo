class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check_sym(root,root)
    def check_sym(self,left,right):
        if not (left and right):
            return left is right
        return left.val==right.val and self.check_sym(left.left,right.right) and self.check_sym(left.right,right.left)
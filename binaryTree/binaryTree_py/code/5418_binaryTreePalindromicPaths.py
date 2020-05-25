# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
from functools import reduce
class Solution:
    def __init__(self):
        self.res = 0
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def traversePath(root, path_dict):
            if root: 
                path_dict[root.val] = path_dict.setdefault(root.val, 0)+1
                if not root.left and not root.right:
                    self.res += 1*self.check(list(path_dict.values()))
                else:
                    traversePath(root.left, copy.copy(path_dict))
                    traversePath(root.right,copy.copy(path_dict))

        self.res = 0
        traversePath(root, dict())
        return self.res

    def check(self, p):
        res = sum(map(lambda x: x%2!=0, p))
        if res > 1:
            return False
        else:
            return True
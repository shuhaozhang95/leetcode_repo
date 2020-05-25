# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def levelOrder01(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = collections.deque([root])
        while q:
            size = len(q)
            curVal = []
            for _ in range(size):
                r = q.popleft()
                curVal.append(r.val)
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
            res.append(curVal)
        return res
    def levelOrder02(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.DFS(root, 0, res)
        return res

    def DFS(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.DFS(root.left, level+1, res)
        if root.right: self.DFS(root.right, level+1, res)

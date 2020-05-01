# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### deque 数据类型来自于collections 模块，支持从头和尾部的常数时间 append/pop 操作。若使用 Python 的 list，通过 list.pop(0) 去除头部会消耗 O(n)O(n) 的时间。
from collections import deque
class Solution:
    ### DFS
    def rightSideView01(self, root):
        right_edge = dict()
        max_depth = -1
        stack = [(root,0)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth,depth)
                right_edge.setdefault(max_depth,node.val)
                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
        return [right_edge[dep] for dep in range(max_depth+1)]

    ### BFS
    def rightSideView02(self, root):
        right_edge = dict()
        max_depth = -1
        queue = deque((root,0))
        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth,depth)
                right_edge[max_depth] = node.val
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return [right_edge[dep] for dep in range(max_depth+1)]
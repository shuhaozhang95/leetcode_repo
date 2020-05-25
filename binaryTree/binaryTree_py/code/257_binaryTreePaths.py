# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def binaryTreePaths01(self, root):
        def construct_paths(root, path):
            if root:
                path.append(root.val)
                if not root.left and not root.right: 
                    paths.append(path) 
                else:
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, [])
        return paths
    def binaryTreePaths02(self, root):
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  
                    paths.append(path) 
                else:
                    path += '->' 
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths

root = TreeNode(2)
a = TreeNode(3)
b = TreeNode(1)
root.left, root.right = a,b
c = TreeNode(3)
d = TreeNode(1)
a.left, a.right = c, d
e = TreeNode(1)
b.right = e

s = Solution()
print(s.binaryTreePaths01(root))
print(s.binaryTreePaths02(root))
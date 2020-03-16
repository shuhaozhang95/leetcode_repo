'''Return the height of a tree'''
def height(root):
    if not root:
        return 0
    else:
        l = 1 + height(root.left)
        r = 1 + height(root.right)
    return max(l,r)
'''Return the length of the longest path in the binary tree'''
def treedis(root):
    if not root:
        return 0
    elif (root.left == None) and (root.right == None):
        return 0
    dis = max(height(root.left)+height(root.right),treedis(root.left),treedis(root.right))
    return dis
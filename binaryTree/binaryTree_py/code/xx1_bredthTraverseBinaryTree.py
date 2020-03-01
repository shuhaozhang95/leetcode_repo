'''Breadth traverse a binary tree'''
def breadth_traverse_1(root):
    current_level = [root]
    next_level = []
    res = []
    while current_level:
        for r in current_level:
            res.append(r.val)
            if r.left:
                next_level.append(r.left)
            if r.right:
                next_level.append(r.right)
        current_level = next_level
        next_level=[]
    return res

def breadth_traverse_2(root):
    x = []
    output = []
    x.append(root)
    prev = 1
    while x:
        n = 0
        for i in range(prev):
            output.append(x[0].val)
            if x[0].left:
                n += 1
                x.append(x[0].left)
            if x[0].right:
                n += 1
                x.append(x[0].right)
            x.pop(0)
        prev = n
    return output
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        store = []
        pre = None
        cur = root
        while cur or store:
            while cur:
                store.append(cur)
                cur = cur.left
            cur = store.pop()
            if pre and cur.val <= pre.val:
                return False
            pre = cur
            cur = cur.right
        return True
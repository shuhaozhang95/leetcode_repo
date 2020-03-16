class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {}
        for i,num in enumerate(inorder):
            dic[num] = i
        store = []
        root = parent = None
        
        for node in preorder:
            newnode = TreeNode(node)
            
            if not root:
                root = parent = newnode
            elif dic[node] < dic[parent.val]:
                parent.left = newnode
                store.append(parent)
            elif dic[node] > dic[parent.val]:
                while store and dic[node] > dic[store[-1].val]:
                    parent = store.pop()
                parent.right = newnode
            parent = newnode
        return root
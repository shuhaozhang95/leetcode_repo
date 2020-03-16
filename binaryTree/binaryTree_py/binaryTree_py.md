# Notes for the LC Problem and Links to the `.py` file

### Definition of Tree: 
    
``` python
'''Binary tree definition and example with root node n1'''
class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(12)
n4 = TreeNode(4)
n5 = TreeNode(7)

n1.left,n1.right = n2,n3
n2.left,n2.right = n4,n5
```

---

### No.xx1 [Bredth traverse](.)

[Link to the Python file](./code/xx1_bredthTraverseBinaryTree.py)

---

### No.xx2 [Get Tree Height and Longest Path](.)

[Link to the Python file](./code/xx2_heightAndLongestPath.py)

**Notes**: 

* Both use recursive method to recurse by the left child and right child

---

### No.xx3 [Check Whether the Tree is Symmetric](.)

[Link to the Python file](./code/xx3_checkSymmetricTree.py)

**Notes**: 

* Should be one of leetcode problem, but cannot recall the problem number. Might add in the future

---

### No.xx4 [Validate a Binary Search Tree](.)

[Link to the Python file](./code/xx4_validateBinarySearchTree.py)

**Notes**: 

* **Definition** of Binary Search Tree: 
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

* This problem also use recursion. To compare: 
    - left.value vs right.value
    - left.left vs right.right
    - left.right vs right.left

* Should be one of leetcode problem, but cannot recall the problem number. Might add in the future

---

### No.xx5 [Contruct Binary Tree from Preorder and Inorder Traverse](.)

[Link to the Python file](./code/xx5_construtFromPreorderInorderTraverse.py)

**Notes**: 

* Should be one of leetcode problem, but cannot recall the problem number. Might add in the future

---

### No.xxx [Template](.)

[Link to the Python file](.)

**Notes**: 

* 

---
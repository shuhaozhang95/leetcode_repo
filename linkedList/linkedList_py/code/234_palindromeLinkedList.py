# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ### Method 1: Store all values and compare with the reversed one
    def isPalindrome01(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
        return vals==vals[::-1]

    ### Method 2: Recursive function method
    def isPalindrome02(self, head: ListNode) -> bool:

    ### Method 3: 
    def isPalindrome03(self, head: ListNode) -> bool:

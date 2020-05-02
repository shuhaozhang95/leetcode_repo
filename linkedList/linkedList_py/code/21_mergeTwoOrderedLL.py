# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ### Method 1: recursion
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: 
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


    ### Method 2: iteration
    def mergeTwoLists02(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        dm = res
        while l1 and l2: 
            if l1.val <= l2.val:
                dm.next = l1
                l1 = l1.next
            else: 
                dm.next = l2
                l2 = l2.next
            dm = dm.next
        dm.next = l1 if l1 else l2
        return res.next
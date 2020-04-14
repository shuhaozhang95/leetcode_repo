# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = [l1.val]
        s2 = [l2.val]
        while l1.next:
            s1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            s2.append(l2.next.val)
            l2 = l2.next
        ansNode = None
        cache = 0
        while s1 or s2 or cache!=0:
            d1 = s1.pop() if s1 else 0
            d2 = s2.pop() if s2 else 0
            current = d1 + d2 + cache
            cache = current // 10
            current = current % 10
            curNode = ListNode(current)
            curNode.next = ansNode
            ansNode = curNode
        return ansNode
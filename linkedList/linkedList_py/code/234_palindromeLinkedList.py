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
        self.front = head 
        def recursive_check(node):
            if node:
                if not recursive_check(node.next):
                    return False
                if self.front.val != node.val:
                    return False
                self.front = self.front.next
            return True
        return recursive_check(head)

    ### Method 3: reverse the second half and check
    def isPalindrome03(self, head: ListNode) -> bool:
        if not head: return True
        if not head.next: return True

        firstEnd = self.firstPartEnd(head)
        secondHead = self.reverseLL(firstEnd.next)

        res = True
        firstPosition = head
        secondPosition = secondHead
        while res and secondPosition:
            if firstPosition.val != secondPosition.val:
                res = False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next
        firstEnd.next = self.reverseLL(secondHead)
        return res

    def reverseLL(self, head):
        prev = None
        current = head
        while current:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        return prev

    def firstPartEnd(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow


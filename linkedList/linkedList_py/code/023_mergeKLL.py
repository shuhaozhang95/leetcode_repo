# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # method 1: use inter to loop
    def mergeKLists01(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length==0:
            return None
        inter = 1
        while inter < length:
            for i in range(0, length-inter, inter*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+inter])
            inter *= 2
        return lists[0]

    # method 2: use left and right index to merge
    def mergeKLists02(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, l, r):
        if l==r: return lists[l]
        if l>r: return None
        mid = (l+r) >> 1
        return self.merge2Lists(self.merge(lists, l,mid), self.merge(lists, mid+1,r))

    def merge2Lists(self, l1, l2):
        pre = ListNode(-1)
        p = pre
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return pre.next
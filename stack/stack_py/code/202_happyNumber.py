 class Solution:
    ### Method 1: use hash set
    '''Note: check existence in hashset is O(1), but in others are O(n)'''
    def isHappyMethod1(self, n):
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = self.nextNum(n)
        return n==1

    def isHappyMethod2(self, n):
        slow = n
        fast = self.nextNum(n)
        while fast !=1 and slow != fast:
            slow = self.nextNum(slow)
            fast = self.nextNum(self.nextNum(fast))
        return fast == 1



    def nextNum(self, num):
        res = 0
        while num > 0:
            num, digit = divmod(num, 10)
            res += digit**2
        return res
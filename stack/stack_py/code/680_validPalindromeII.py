class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.checkSymmetric(low+1, high,s) or self.checkSymmetric(low, high-1,s)
        return True
        
    def checkSymmetric(self, l, r, s):
        while l<r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True

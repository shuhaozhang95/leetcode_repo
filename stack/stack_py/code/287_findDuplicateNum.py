class Solution:
    ## Binary Search
    def findDuplicate01(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            cnt = sum(map(lambda x: x<=mid,nums))
            if cnt <= mid: 
                l = mid+1 
            else:
                r = mid-1
                res = mid
        return res
    ## Binary Operation
    def findDuplicate02(self, nums: List[int]) -> int:
        n = len(nums)
        maxBit = len(bin(n-1))-2
        ans = 0
        for b in range(maxBit+1):
            x, y = 0, 0
            for i in range(n):
                if nums[i] & (1<<b):
                    x+=1
                if i>0 and (i & (1<<b)):
                    y+=1
            if x > y:
                ans |= (1<<b)
        return ans
    ## fast and slow pointer
    def findDuplicate03(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution:
    ### Summary: 
    ######## * need to have the definition of dp function at the start
    ######## * iter at index i, compare subarray till i and i itself
    ### Method 1: dynamic programming
    def maxSubArray01(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        dp = nums[:]
        res = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])
        return res
    ### Method 2: dynamic programming with no extra storage
    ###### adjust on the given array
    def maxSubArray02(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        res = nums[0]
        for i in range(1,n):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
            res = max(res, nums[i])
        return res

    ### Method 3: violent
    def maxSubArray03(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        n = len(nums) 
        tmp = nums[0]
        res = tmp
        for i in range(1,n):
            if tmp+nums[i] > nums[i]:
                res = max(res, tmp+nums[i])
                tmp += nums[i]
            else:
                res = max(res, nums[i])
                tmp = nums[i]
        return res  

    ### Method 4: Recursion, bisect the array till only one left
    ######## max subarray (1) at left, (2) at right  and (3)in the middle

    def maxSubArray04(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        else:
            maxLeft = self.maxSubArray04(nums[:n//2])
            maxRight = self.maxSubArray04(nums[n//2:n])
        max_l = nums[(n//2)-1]
        tmp = 0
        for i in range(n//2-1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[(n//2)]
        tmp = 0
        for i in range(n//2, n):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(maxLeft, maxRight, max_l+max_r)

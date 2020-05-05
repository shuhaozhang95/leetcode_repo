class Solution:
    ### * greed in the original order, count the furthest pos which num can reach
    ### * only add 1 to step when the boundary (previous furthest pos) is reached
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, res = 0, 0, 0
        for i in range(n-1):
            if maxPos>=i:
                maxPos = max(maxPos, i+nums[i])
            if i==end:
                end = maxPos
                res += 1
        return res

    ## Backtrack from end, but will return RE with python
    def jump02(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        dp = [0]+ [s]*(n-1)
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]>=i-j:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[n-1]

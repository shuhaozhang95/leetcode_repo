class Solution:

    def maxProduct01(self, nums: List[int]) -> int:
        N = len(nums)
        dp_max = [nums[0]]*N
        dp_min = [nums[0]]*N
        res = nums[0]
        for i in range(1,N):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            res = max(res, dp_max[i])
        return res

    def maxProduct02(self, nums: List[int]) -> int:
        N = len(nums)
        curMax, curMin, res= nums[0], nums[0], nums[0]
        for i in range(1,N):
            prevMax, prevMin = curMax, curMin
            curMax = max(prevMax*nums[i], prevMin*nums[i], nums[i])
            res = max(curMax, res)
            curMin = min(prevMax*nums[i], prevMin*nums[i], nums[i])
        return res

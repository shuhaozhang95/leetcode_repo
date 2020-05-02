class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def recur(first=0):
            if first==n: 
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                recur(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        recur()
        return res

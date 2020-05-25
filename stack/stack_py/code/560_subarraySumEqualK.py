class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        N = len(nums)
        cur, res = 0, 0
        for i in range(N):
            cur += nums[i]
            res += hm.setdefault(cur-k,0)
            hm[cur] = hm.setdefault(cur,0)+1
        return res

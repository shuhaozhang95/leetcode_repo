class Solution:
    ### Method 1: dp by all days in a year
    def mincostTickets01(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        validaty = [1,7,30]
        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i+l)+c for l,c in zip(validaty,costs))
            else:
                return dp(i+1)
        return dp(1)


    ### Method 2: dp by all travels days given
    def mincostTickets02(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        validaty = [1,7,30]
        @lru_cache(None)
        def dp(i):
            if i>=N:
                return 0
            res = 10**9
            j = i
            for l,c in zip(validaty,costs):
                while j < N and days[j] < days[i]+l:
                    j+=1
                res = min(res, dp(j)+c)
            return res
        return dp(0)
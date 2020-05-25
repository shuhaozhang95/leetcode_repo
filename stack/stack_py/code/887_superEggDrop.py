class Solution:
    ### Method 1: normal method
    def superEggDrop01(self, K: int, N: int) -> int:
        memory = {}
        def dp(k,n):
            if (k,n) not in memory:
                if n==0:
                    ans = 0
                elif k==1:
                    ans = n 
                else:
                    l, h = 1, n
                    while l+1 < h:
                        x = (l+h) // 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)
                        if t1 < t2:
                            l = x
                        elif t1 > t2:
                            h = x
                        else:
                            l = h = x
                    ans = 1 + min(max(dp(k-1, x0-1), dp(k, n-x0)) for x0 in (l,h))
                memory[k,n] = ans
            return memory[k,n]
        return dp(K,N)
    ### Method 2: Monotonic Decision
    def superEggDrop02(self, K: int, N: int) -> int:
        dp = list(range(N+1))
        dpNext = [0]*(N+1)
        for k in range(2,K+1):
            x = 1
            for n in range(1, N+1):
                while x<n and max(dp[x-1], dpNext[n-x]) >= max(dp[x], dpNext[n-x-1]):
                    x+=1
                dpNext[n] = 1 + max(dp[x-1], dpNext[n-x])
            dp = dpNext[:]
        return dp[-1]
    ### Method 3: inverse thinking
    def superEggDrop03(self, K: int, N: int) -> int:
        if N==1: return 1
        f = [[0]*(K+1) for _ in range(N+1)]
        for k in range(1,K+1):
            f[1][k] = 1
        res = -1
        for i in range(2, N+1):
            for k in range(1,K+1):
                f[i][k] = 1 + f[i-1][k] + f[i-1][k-1]
            if f[i][K] >= N:
                res = i
                break
        return res

class Solution:
    # Dynamic Programming method
    def waysToChange01(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25,10,5,1]
        store = [1] + [0]*n
        for coin in coins:
            for i in range(coin,n+1):
                store[i] += store[i-coin]
        return store[n] % mod
    # Maths method
    def waysToChange02(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(n//25 + 1):
            r = n - 25*i
            a, b = r//10, r%10 // 5
            ans += (a+1) * (a+b+1)
        return ans % mod

class Solution:

    def myPow01(self, x: float, n: int) -> float:
        def mul(N):
            if N==0:
                return 1.0
            y = mul(N//2)
            return y * y if N % 2 == 0 else y * y * x
        return mul(n) if n>=0 else 1.0 / mul(-n)


    def myPow02(self, x: float, n: int) -> float:
        def mul(N):
            ans = 1.0
            x_contrib = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contrib
                x_contrib *= x_contrib
                N //= 2
            return ans
        return mul(n) if n>=0 else 1.0/mul(-n)
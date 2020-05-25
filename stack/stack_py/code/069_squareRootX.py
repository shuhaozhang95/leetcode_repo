import math
class Solution:
    ### Method 01: exp(0.5lnx)
    def mySqrt01(self, x: int) -> int:
        if x==0:
            return 0
        res = int(math.exp(0.5*math.log(x)))
        # because exp and log are floating operation, error exist when only remain the int part
        if (res+1)**2 <= x:
            return res+1
        else:
            return res

    ### Method 02: binary search        
    def mySqrt02(self, x: int) -> int:
        if x==0:
            return 0
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid**2 <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid-1
        return ans

    ### Method 03: Newton iteration x1 = 0.5*(x0+C/x0) 
    def mySqrt03(self, x: int) -> int:
        if x==0:
            return 0
        x0,C = float(x), float(x)
        while True:
            xi = 0.5*(x0+(C/x0))
            if abs(x0-xi) < 1e-7:
                break
            x0 = xi
        return int(x0)

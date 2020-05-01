import functools
class Solution:
    def singleNumbers(self, nums):
        # reduce will execuate the operation pair by pair
        # XOR is independent to order, so XOR between same number will become 0 and ret is left with the 
            # XOR value between a and b
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        # use div to find the binary digit where x and y are different
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

s = Solution()
s.singleNumbers([4,1,4,6,6,8])
import bisect
class BIT:
    def __init__(self, n):
        self.n = n 
        self.tree = [0]*(n+1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self,x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= BIT.lowbit(x)
        return res

    def update(self,x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)

class Solution:
    def reversePairs(self, nums):
        n = len(nums)
        # discretize
        tmp = sorted(nums)
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1

        bit = BIT(n)
        ans = 0
        for i in range(n-1, -1, -1):
            ans += bit.query(nums[i] - 1)
            bit.update(nums[i])
        return ans
            

    def reversePairs_MS(self, nums):
        if len(nums) <= 1: return 0
        cnt = self.mergeSortAndCount(nums, 0)
        return cnt

    def mergeSortAndCount(self, arr, counter):
        if len(arr)>1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            cnt_left = self.mergeSortAndCount(left, counter)
            cnt_right = self.mergeSortAndCount(right, counter)
            counter = cnt_left + cnt_right

            i, j = 0, 0
            left.append(float('inf'))
            right.append(float('inf'))
            for k in range(len(arr)):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    counter += j
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
        return counter

s = Solution()
res = s.reversePairs([7,5,6,4])
print(res)
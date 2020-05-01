class Solution:
    # maths mehtod
    def numberOfSubarrays01(self, nums: List[int], k: int) -> int:
        odd = [-1]
        res = 0
        for i in range(len(nums)):
            if (nums[i]%2) == 1:
                odd.append(i)
        odd.append(len(nums))
        for j in range(1, len(odd)-k):
            res += (odd[j]-odd[j-1])*(odd[j+k]-odd[j+k-1])
        return res
        
    # prefix + diff mehtod
    def numberOfSubarrays02(self, nums: List[int], k: int) -> int:
        count = [0] * (len(nums)+1)
        count[0] = 1
        odd, res = 0, 0
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odd +=1
            if odd >= k:
                res += count[odd-k]
            count[odd] += 1

        return res
class Solution:
    def binarySearch(self, mountain, target, l, r, key=lambda x: x):
        target = key(target)
        while l <= r:
            mid = (l + r) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        index = self.binarySearch(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = self.binarySearch(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index
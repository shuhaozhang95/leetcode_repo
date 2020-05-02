class Solution:

    # Method 1: Use set to loop left pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk < n-1 and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans


    # Method 2: Use dict to loop right pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(set(s))==1:
            return 1
        store = {s[0]:0}
        start = 0
        max_len = 0
        for end in range(1, len(s)):
            if s[end] not in store:
                store[s[end]] = end
                max_len = max(max_len, end-start+1)
            else:
                start = max(store[s[end]]+1, start)
                store[s[end]] = end
                max_len = max(max_len, end-start+1)
        return max_len
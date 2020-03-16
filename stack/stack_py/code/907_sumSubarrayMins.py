class Solution:
    # Maintain Stack of Minimums
    def sumSubarrayMins_1(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = 0
        temp = 0
        for idx,n in enumerate(A):
            cnt = 1
            while stack and stack[-1][-1] >= n:
                c,x = stack.pop()
                cnt += c
                temp -= c*x
            stack.append((cnt,n))
            temp += cnt*n
            res += temp
        return res % MOD
    # Prev/Next Array
    def sumSubarrayMins_2(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        # prev
        stack = []
        prev = [None]*N
        for i in range(N):
            while stack and A[i]<=A[stack[-1]]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            else:
                prev[i] = -1
            stack.append(i)
        # next
        stack = []
        next_ = [None]*N
        for j in range(N-1,-1,-1):
            while stack and A[j]<A[stack[-1]]:
                stack.pop()
            if stack:
                next_[j] = stack[-1]
            else:
                next_[j] = N
            stack.append(j)
        
        res = 0
        for i in range(N):
            res += (i-prev[i]) * (next_[i]-i) * A[i]
        return res % MOD

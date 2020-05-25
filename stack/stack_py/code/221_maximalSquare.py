class Solution:
    ### Method 01: brute force
    def maximalSquare01(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0
        maxSide = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    maxSide = max(maxSide, 1)
                    currentMaxSide = min(rows-i, cols-j)
                    for k in range(1, currentMaxSide):
                        flag = True
                        if matrix[i+k][j+k] == '0':
                            break
                        for m in range(k):
                            if matrix[i+k][j+m]=='0' or matrix[i+m][j+k]=='0':
                                flag = False
                                break
                        if flag: 
                            maxSide = max(maxSide, k+1)
                        else:
                            break
        return maxSide*maxSide
    ### Method 02: dynamic programming
    ##### dp[i][j] means the maxside length of square with (i,j) as right bottom corner
    def maximalSquare02(self, matrix):
        maxSide = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide*maxSide
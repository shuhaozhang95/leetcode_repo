import collections
class Solution:
    ### Method: BFS
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1: q.append((i,j))
        if len(q)==0 or len(q)==N*N: return -1
        res = -1
        while len(q) > 0:
            res += 1
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                # left
                if r-1 >= 0 and grid[r-1][c]==0:
                    grid[r-1][c] = 2
                    q.append((r-1,c))
                # up
                if c-1 >= 0 and grid[r][c-1]==0:
                    grid[r][c-1] = 2
                    q.append((r,c-1))
                # right
                if r+1 < N and grid[r+1][c]==0:
                    grid[r+1][c] = 2
                    q.append((r+1,c))
                # down
                if c+1 < N and grid[r][c+1]==0:
                    grid[r][c+1] = 2
                    q.append((r,c+1))
        return res

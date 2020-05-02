class Solution:

    # Method 1: Breadth First Search (BFS)
    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0]*n for _ in range(m)]
        zero_pos = [(i,j) for i in range(m) for j in range(n) if matrix[i][j]==0]
        seen_pos = set(zero_pos)

        stack = copy(zero_pos)
        while stack: 
            i, j = stack.pop(0)
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen_pos:
                    dist[ni][nj] = dist[i][j] + 1
                    stack.append((ni,nj))
                    seen_pos.add((ni,nj))
        return dist

    # Method 2: DP (can only have two directions)
    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[10**9]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # up and left only
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                if j-1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1]+1)
        # down and right
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1 < m:
                    dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
                if j+1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j+1]+1)
        return dist
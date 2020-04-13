class Solution:
    # DFS
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i,j,s_i,s_j):
            if i>=m or j>=n or (s_i+s_j)>k or (i,j) in visited: 
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1,j,s_i+1 if (i+1) %10 else s_i-8,s_j) + dfs(i,j+1,s_i,s_j+1 if (j+1)%10 else s_j-8)
        visited = set()
        return dfs(0,0,0,0)
    # BFS
    def movingCount_BFS(self,m,n,k):
        Q, visited = [(0, 0, 0, 0)], set()
        while Q:
            i,j,s_i,s_j = Q.pop(0)
            if i>=m or j>=n or (s_i+s_j)>k or (i,j) in visited:
                continue
            visited.add((i,j))
            Q.append((i+1,j,s_i+1 if (i+1)%10 else s_i-8,s_j))
            Q.append((i,j+1,s_i,s_j+1 if (j+1)%10 else s_j-8))
        return len(visited)

    def digitSum(self, x):
        return sum(map(int,list(str(x))))
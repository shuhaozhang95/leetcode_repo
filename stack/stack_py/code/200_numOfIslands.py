# Method 1: DFS
class SolutionDFS:
    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]: 
            if 0<=x<nr and 0<=y<nc and grid[x][y]=="1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        res  = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    res += 1
                    self.dfs(grid, r, c)
                    
        return res

# Method 2: BFS
import collections
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        res  = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    res += 1
                    grid[r][c]="0"
                    neighbors = collections.deque([(r,c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if 0<=x<nr and 0<=y<nc and grid[x][y]=="1":
                                neighbors.append((x,y))
                                grid[x][y]="0"
        return res

# Method 3: Union search
class UnionFind:
    def __init__(self, grid):
        nr, nc = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (nr*nc)
        self.rank = [0] * (nr*nc)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=="1":
                    self.parent[r*nc+c] = r*nc+c 
                    self.count += 1
    def findParent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.findParent(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        rootx = self.findParent(x)
        rooty = self.findParent(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                        if 0<=x<nr and 0<=y<nc and grid[x][y]=="1":
                            uf.union(r*nc+c,x*nc+y)

        return uf.getCount()

import collections
class Solution:
    ### Method01: DFS
    def findOrder01(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = dict()
        for c in prerequisites:
            edges[c[1]] = edges.setdefault(c[1],[]) + [c[0]]
        visited = [0]*numCourses
        invalid = False
        res = []
        def dfs(c):
            nonlocal invalid
            visited[c] = 1
            if c in edges:
                for e in edges[c]:
                    if visited[e]==0:
                        dfs(e)
                        if invalid:
                            return
                    elif visited[e]==1:
                        invalid = True
                        return
            visited[c]=2
            res.append(c)
        for i in range(numCourses):
            if not invalid and not visited[i]:
                dfs(i)
        if invalid:
            return []
        return res[::-1]
    ### Method02: BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indeg = [0]*numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]]+=1
        q = collections.deque([u for u in range(numCourses) if indeg[u]==0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for e in edges[c]:
                indeg[e] -= 1
                if indeg[e]==0:
                    q.append(e)
        if len(res) != numCourses:
            return []
        return res

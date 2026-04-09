class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_deg = [0] * numCourses
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            in_deg[pre] += 1
            adj[crs].append(pre)
        
        q = deque()
        res = []

        for crs in range(numCourses):
            if in_deg[crs] == 0:
                q.append(crs)

        while q:
            crs = q.popleft()

            res.append(crs)

            for dep in adj[crs]:
                in_deg[dep] -= 1

                if in_deg[dep] == 0:
                    q.append(dep)
        if len(res) != numCourses:
            return []
        return res[::-1]

        
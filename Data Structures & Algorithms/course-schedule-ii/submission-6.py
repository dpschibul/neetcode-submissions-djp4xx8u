class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        indegree = [0] * numCourses

        for nxt, pre in prerequisites:
            adj[pre].append(nxt)
            indegree[nxt] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        
        while q:
            crs = q.popleft()

            res.append(crs)

            for nxt in adj[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if len(res) != numCourses:
            return []
        return res


        
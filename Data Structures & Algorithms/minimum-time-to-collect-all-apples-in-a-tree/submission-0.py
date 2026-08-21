class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        apples = []

        for i, is_apple in enumerate(hasApple):
            if is_apple:
                apples.append(i)

        def findShortestPath(f, to):

            q = deque()
            q.append(f)
            visit = set()

            steps = 0

            while q:
                length = len(q)
                for _ in range(length):
                    node = q.popleft()
                    if node in apples:
                        apples.remove(node)
                        return [steps, node]
                    if node == to:
                        return [steps, node]

                    visit.add(node)

                    for nei in adj[node]:
                        if nei in visit:
                            continue
                        q.append(nei)
                
                steps += 1
            return [-1, -1]
        res = 0
        start = 0
        while apples:
            steps, end = findShortestPath(start, -1)
            start = end
            res += steps
        
        return res + findShortestPath(start, 0)[0]
        








        
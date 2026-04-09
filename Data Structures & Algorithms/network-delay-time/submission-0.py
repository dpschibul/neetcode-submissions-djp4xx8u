class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for ui, vi, ti in times:
            edges[ui].append((vi, ti))
        
        minHeap = [(0, k)]

        visit = set()
        t = 0

        while minHeap:
            ti, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            t = ti
            visit.add(node)

            for edge in edges[node]:
                if edge[0] not in visit:
                    heapq.heappush(minHeap, (edge[1] + ti, edge[0]))
        
        if len(visit) == n:
            return t
        return -1


        
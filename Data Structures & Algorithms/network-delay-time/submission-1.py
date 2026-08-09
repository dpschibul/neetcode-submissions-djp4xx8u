class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        min_heap = [(0, k)]
        visit = set()
        t = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)

            t = cost

            for nei, nei_cost in adj[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (cost + nei_cost, nei))
        return t if len(visit) == n else -1
        
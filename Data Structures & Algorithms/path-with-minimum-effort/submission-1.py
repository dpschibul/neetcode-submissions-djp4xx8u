class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [(0, ROWS-1, COLS-1)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if (r, c) in visit:
                continue
            
            visit.add((r, c))
            
            if (r, c) == (0, 0):
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit:
                    continue
                newDiff = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap, (newDiff, nr, nc))
        
        return 0
        
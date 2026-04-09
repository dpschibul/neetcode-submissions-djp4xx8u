class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        heapq.heappush(minHeap, [0, (0, 0)])
        visit = set()

        while minHeap:
            cost, pos = heapq.heappop(minHeap)

            if pos in visit:
                continue
            
            visit.add(pos)

            if pos == (ROWS - 1, COLS -1):
                return cost
            
            for dr, dc in directions:
                row = pos[0] + dr
                col = pos[1] + dc
                if row >= 0 and col >=0 and row < ROWS and col < COLS and (row, col) not in visit:
                    newDiff = max(cost, abs(heights[pos[0]][pos[1]] - heights[row][col]))
                    heapq.heappush(minHeap, [newDiff, (row, col)])
        return 0
            




        
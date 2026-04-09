class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        SIZE = len(grid)
        heap = [[grid[0][0], 0, 0]]
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while heap:
            height, row, col = heapq.heappop(heap)

            if row == SIZE-1 and col == SIZE-1:
                return height
            
            visit.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE or (nr, nc) in visit:
                    continue
                heapq.heappush(heap, [max(height, grid[nr][nc]), nr, nc])

    
    # [[0,1,2,10],
    #  [9,14,4,13],
    #  [12,3,8,15],
    #  [11,5,7,6]]]
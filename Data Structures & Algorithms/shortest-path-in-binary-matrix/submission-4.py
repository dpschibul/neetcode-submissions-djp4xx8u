class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]] 
        n = len(grid)
        q = deque()
        q.append((0, 0, 0))
        visit = set()

        if grid[0][0] == 1:
            return -1
        
        while q:
            length = len(q)
            for i in range(length):
                r, c, s = q.popleft()
                
                if (r, c) == (n - 1, n - 1):
                    return s + 1
                visit.add((r, c))

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or nr >= n or 
                    nc >= n or (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    
                    q.append((nr, nc, s + 1))

        return -1
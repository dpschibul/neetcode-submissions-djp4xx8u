
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        starting_island = set() # row, col

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or (r, c) in starting_island or grid[r][c] == 0:
                return
            
            starting_island.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            if starting_island:
                break
        
        shortest_bridge = 0

        q = deque(starting_island)
        visited = set()

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visited or (nr, nc) in starting_island:
                        continue
                    
                    if grid[nr][nc] == 1:
                        return shortest_bridge
                    visited.add((nr, nc))
                    q.append((nr, nc))
                
            shortest_bridge += 1
    
        return -1
        
        
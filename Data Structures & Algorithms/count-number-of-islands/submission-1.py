class Solution:
    def numIslands(self, grid: list[list[int]]) -> int:
	
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def bfs(r: int, c: int) -> None:
            grid[r][c] = "0"
            
            q = deque()
            
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dir in directions:
                    nr, nc = dir[0] + row, dir[1] + col
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count

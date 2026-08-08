class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        islands = 0
        seen = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in seen:
                return
            
            seen.add((r,c))

            for dir in directions:
                dfs(r + dir[0], c + dir[1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
        return islands

        
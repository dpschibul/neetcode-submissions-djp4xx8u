class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == len(grid) or
             c == len(grid[0]) or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            count = 1
            for nr, nc in directions:
                count += dfs(nr + r, nc + c)
            return count

        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r, c))

        return area


        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxIsland = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j) -> int:
            nonlocal maxIsland
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            area = 1
            
            for dir in directions:
                area += dfs(i+dir[0], j+dir[1])
            return area
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxIsland = max(dfs(i, j), maxIsland)
        
        return maxIsland

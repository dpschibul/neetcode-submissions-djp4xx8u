class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def deleteIsland(i, j):
            if (i < 0 or j < 0 or 
            i >= len(grid) or j >= len(grid[0]) or
            grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"

            deleteIsland(i-1, j)
            deleteIsland(i+1, j)
            deleteIsland(i, j-1)
            deleteIsland(i, j+1)

        islands = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "1":
                    islands+=1
                    deleteIsland(i, j)

        return islands


        
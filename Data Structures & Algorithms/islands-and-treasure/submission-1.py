class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1,0], [1,0], [0, -1], [0, 1]]
        
        def markDistance(r, c, dist):  # grid[r,c]=3, dist =1
            if (r < 0 or 
                c < 0 or 
                r >= len(grid) or 
                c >= len(grid[0]) or
                grid[r][c] < dist):
                return 
            
            grid[r][c] = dist

            for dir in directions:
                markDistance(r + dir[0], c + dir[1], dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    for dir in directions:
                        markDistance(i + dir[0], j + dir[1], 1)



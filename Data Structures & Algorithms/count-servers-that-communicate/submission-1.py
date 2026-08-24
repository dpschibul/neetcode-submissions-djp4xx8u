class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count_row_servers = [0] * ROWS
        count_col_servers = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count_row_servers[r] += 1
                    count_col_servers[c] += 1
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and max(count_row_servers[r], count_col_servers[c]) > 1:
                    count += 1
        return count
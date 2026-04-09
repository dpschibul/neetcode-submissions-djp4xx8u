class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def update_map(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                update_map(r-1, c)
                update_map(r+1, c)
                update_map(r, c-1)
                update_map(r, c+1)
            
            dist += 1


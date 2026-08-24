class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        starting_island = set()

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= n or c >= n or
                (r, c) in starting_island or
                grid[r][c] == 0
            ):
                return

            starting_island.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Find first island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            if starting_island:
                break

        # Multi-source BFS
        q = deque(starting_island)
        visited = set(starting_island)
        bridge_len = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= n or nc >= n or
                        (nr, nc) in visited
                    ):
                        continue

                    # Found second island
                    if grid[nr][nc] == 1:
                        return bridge_len

                    visited.add((nr, nc))
                    q.append((nr, nc))

            bridge_len += 1

        return -1
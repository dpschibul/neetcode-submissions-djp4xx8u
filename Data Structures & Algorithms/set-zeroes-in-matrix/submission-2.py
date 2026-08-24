class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = set()
        originals = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    originals.add((r, c))

        def dfs(r, c, vertical):
            if (r < 0 or r >= len(matrix) or 
                c < 0 or c >= len(matrix[0]) or 
                (r, c, vertical) in visited):
                return

            matrix[r][c] = 0
            visited.add((r, c, vertical))

            if vertical:
                dfs(r + 1, c, vertical)
                dfs(r - 1, c, vertical)
            else:
                dfs(r, c + 1, vertical)
                dfs(r, c - 1, vertical)

        for r, c in originals:
            dfs(r, c, True)
            dfs(r, c, False)
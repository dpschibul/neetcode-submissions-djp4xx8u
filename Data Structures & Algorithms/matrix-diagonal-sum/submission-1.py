class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        seen = set()

        def dfs(r, c, is_primary):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if (r,c) in seen:
                return dfs(r + 1 if is_primary else r - 1, c + 1, is_primary)
            seen.add((r, c))
            return mat[r][c] + dfs(r + 1 if is_primary else r - 1, c + 1, is_primary)
        
        return dfs(0, 0, True) + dfs(ROWS-1, 0, False)


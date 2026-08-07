class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = set()
        res = []

        r, c = 0, 0
        dir_index = 0
        dir = directions[0]

        while len(seen) < len(matrix) * len(matrix[0]):
            seen.add((r, c))
            res.append(matrix[r][c])

            nr = r + directions[dir_index][0]
            nc = c + directions[dir_index][1]

            # Turn if next position is invalid or already visited
            if (
                nr < 0 or nr >= len(matrix) or
                nc < 0 or nc >= len(matrix[0]) or
                (nr, nc) in seen
            ):
                dir_index = (dir_index + 1) % 4
                nr = r + directions[dir_index][0]
                nc = c + directions[dir_index][1]

            r, c = nr, nc


        return res
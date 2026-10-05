class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if boxGrid[r][c] == "#":
                    move = c
                    for sc in range(c + 1, COLS):
                        if boxGrid[r][sc] == "*":
                            break
                        if boxGrid[r][sc] == ".":
                            move = sc
                    boxGrid[r][c], boxGrid[r][move] = boxGrid[r][move], boxGrid[r][c]
        res = []

        for c in range(COLS):
            cur = []
            for r in range(ROWS-1, -1, -1):
                cur.append(boxGrid[r][c])
            res.append(cur)

        return res
        
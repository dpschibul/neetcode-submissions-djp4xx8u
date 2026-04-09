class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atlantic = set()
        pacific = set()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(i, j, sea, prevHeight):
            if (i < 0 or i == len(heights) or j < 0 or j == len(heights[0]) or
                heights[i][j] < prevHeight) or (i, j) in sea:
                return

            sea.add((i, j))

            for di, dj in directions:
                dfs(i + di, j + dj, sea, heights[i][j])

        for i in range(len(heights)):
            dfs(i, 0, pacific, -1)
            dfs(i, len(heights[0])-1, atlantic, -1)

        for i in range(len(heights[0])):
            dfs(0, i, pacific, -1)
            dfs(len(heights)-1, i, atlantic, -1)

        res = []
        for pos in atlantic:
            if pos in pacific:
                res.append([pos[0], pos[1]])

        return res


        
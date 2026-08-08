class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, col):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != col or image[r][c] == color:
                return

            image[r][c] = color

            for dir in directions:
                dfs(r + dir[0], c + dir[1], col)
        
        dfs(sr, sc, image[sr][sc])
        return image
        
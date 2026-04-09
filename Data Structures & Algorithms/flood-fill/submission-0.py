class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([(sr, sc)])
        visited = set()
        org_color = image[sr][sc]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r >= len(image) or c >= len(image[0]) or
                    r < 0 or c < 0 or (r, c) in visited or image[r][c] != org_color):
                    continue
                visited.add((r, c))
                image[r][c] = color

                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))

        return image

                

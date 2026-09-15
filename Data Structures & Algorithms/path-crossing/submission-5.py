class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        visit = {(0, 0)}
        x, y = 0, 0

        for direction in path:
            dx, dy = directions[direction]

            x += dx
            y += dy

            if (x, y) in visit:
                return True
            
            visit.add((x, y))
        
        return False
        
        
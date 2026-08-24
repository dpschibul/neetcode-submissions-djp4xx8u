class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ROWS = len(wall)
        count = defaultdict(int)

        for r in range(ROWS):
            for c in range(len(wall[r]) - 1):
                wall[r][c] = (wall[r][c-1] + wall[r][c]) if c > 0 else wall[r][c]
                count[wall[r][c]] += 1

        return ROWS - (max(count.values()) if count else 0)

        
        # [[1,2,2,1],
        # [3,1,2],
        # [1,3,2],
        # [2,4],
        # [3,1,2],
        # [1,3,1,1]]

        # [[1,3,5,6],
        # [3,4,6],
        # [1,4,6],
        # [2,6],
        # [3,4,6],
        # [1,4,5,6]]

        # {1: 2, 2: 1, 3: 3, 5: 1, 4: 4}

        # num rows - max(dict.values())
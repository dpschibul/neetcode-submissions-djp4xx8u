class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (r-l)//2+l
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid+1
            else:
                r = mid-1
        return False


        
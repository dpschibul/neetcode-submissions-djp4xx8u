class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            r_count=0
            for c in range(len(matrix[0])):
                above = 0
                if r > 0:
                    above += self.matrix_sum[r-1][c]
                r_count += matrix[r][c]
                self.matrix_sum[r][c] = above + r_count


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix_sum[row2][col2]
        if row1 > 0:
            res -= self.matrix_sum[row1-1][col2]
        if col1 > 0:
            res -= self.matrix_sum[row2][col1-1]
        if col1 > 0 and row1 > 0:
            res += self.matrix_sum[row1-1][col1-1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for r in range(len(matrix)):
            row_sum = 0
            for c in range(len(matrix[0])):
                val = self.matrix[r][c] + row_sum
                if r > 0:
                    val += self.matrix[r-1][c]
                row_sum += self.matrix[r][c]
                self.matrix[r][c] = val


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]

        if row1 > 0 and col1 > 0:
            res += self.matrix[row1-1][col1-1]
        if row1 > 0:
            res -= self.matrix[row1-1][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1-1]
        return res
            
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
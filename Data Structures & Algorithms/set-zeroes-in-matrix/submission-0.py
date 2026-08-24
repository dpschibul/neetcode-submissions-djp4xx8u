class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0
        

        





        
        
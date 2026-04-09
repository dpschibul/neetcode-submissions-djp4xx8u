class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         rows = []
         cols = []

         for rowIndex, row in enumerate(board):
            rows.append([])
            for value in row:
                if value.isdigit() != True :
                    continue
                if value in rows[rowIndex]:
                    return False
                rows[rowIndex].append(value)
        
         for j in range(9):
            cols.append([])
            for i in range(9):
                if board[i][j].isdigit() != True:
                    continue
                
                if board[i][j] in cols[j]:
                    return False
                cols[j].append(board[i][j])

         boxes = []
         currBox = 0
         for i in range(3):
            for j in range (3):
                boxes.append([])
                for c in range(3):
                    for r in range(3):
                        xPos = i*3+c
                        yPos = j*3+r
                        if board[xPos][yPos].isdigit() != True:
                            continue
                        if board[xPos][yPos] in boxes[currBox]:
                            return False
                        boxes[currBox].append(board[xPos][yPos])
                currBox+=1


         return True
                

        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        boardering_regions = set()

        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i < 0 or i == len(board) or j < 0 or 
            j == len(board[0]) or board[i][j] != "O" or 
            (i, j) in boardering_regions):
                return 
            boardering_regions.add((i,j))

            for di, dj in directions:
                dfs(i + di, j + dj)
        
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0])-1] == "O":
                dfs(i, len(board[0])-1)
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0,i)
            if board[len(board)-1][i] == "O":
                dfs(len(board)-1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in boardering_regions:
                    board[i][j] = "X"
        




        
        
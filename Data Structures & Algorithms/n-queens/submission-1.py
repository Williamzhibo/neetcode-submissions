class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() #
        negDiag = set()

        board = [['.'] * n for i in range(n)] #build nxn board 

        result = []
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in cols or (row + c) in posDiag or (row - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'

                backtrack(row + 1)

                cols.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)

                board[row][c] = '.'
        backtrack(0)
        return result
            
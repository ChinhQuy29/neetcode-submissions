class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        col = [False] * n
        posDiag = [False] * (2 * n)
        negDiag = [False] * (2 * n)

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if col[c] or posDiag[r + c] or negDiag[r - c + n]:
                    continue
                
                if self.isSafe(r, c, board):
                    col[c] = True
                    posDiag[r + c] = True
                    negDiag[r - c + n] = True
                    board[r][c] = "Q"

                    backtrack(r + 1)

                    col[c] = False
                    posDiag[r + c] = False
                    negDiag[r - c + n] = False
                    board[r][c] = "."

        backtrack(0)
        return res

    def isSafe(self, r: int, c: int, board) -> bool:
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0 :
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True
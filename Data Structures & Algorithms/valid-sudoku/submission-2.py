class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkCol(board: List[List[str]]) -> bool:
            for i in range(9):
                num_set = set()
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] in num_set:
                        return False
                    num_set.add(board[j][i])
            return True

        def checkRow(board: List[List[str]]) -> bool:
            for i in range(9):
                num_set = set()
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
            return True

        def checkBox(board: List[List[str]]) -> bool:
            for i in range(0, 9, 3):             
                for j in range(0, 9, 3):
                    num_set = set()
                    for k in range(3):
                        for r in (i, i + 1, i + 2):
                            if board[r][j + k] == ".":
                                continue
                            if board[r][j + k] in num_set:
                                return False
                            num_set.add(board[r][j + k])
            return True
                    
        return checkCol(board) and checkRow(board) and checkBox(board)
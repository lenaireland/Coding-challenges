class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        Determine if a 9x9 Sudoku board is valid. Only the filled cells need to 
        be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 
        without repetition.

        A partially filled sudoku which is valid.

        The Sudoku board could be partially filled, where empty cells are 
        filled with the character '.'.
        """
        
        nums = set(['1','2','3','4','5','6','7','8','9'])
        
        for i in range(9):
            row_nums = nums.copy()
            column_nums = nums.copy()
            for j in range(9):
                if board[i][j] in row_nums:
                    row_nums.remove(board[i][j])
                elif board[i][j] != ".":
                    return False
                
                if board[j][i] in column_nums:
                    column_nums.remove(board[j][i])
                elif board[j][i] != ".":
                    return False
                
        for n in range(3):
            for m in range(3):
                square_nums = nums.copy()
                
                if board[n*3][m*3] in square_nums:
                    square_nums.remove(board[n*3][m*3])
                elif board[n*3][m*3] != ".":
                    return False

                if board[n*3 + 1][m*3] in square_nums:
                    square_nums.remove(board[n*3 + 1][m*3])
                elif board[n*3 + 1][m*3] != ".":
                    return False
                
                if board[n*3 + 2][m*3] in square_nums:
                    square_nums.remove(board[n*3 + 2][m*3])
                elif board[n*3 + 2][m*3] != ".":
                    return False
                
                if board[n*3][m*3 + 1] in square_nums:
                    square_nums.remove(board[n*3][m*3 + 1])
                elif board[n*3][m*3 + 1] != ".":
                    return False
                
                if board[n*3 + 1][m*3 + 1] in square_nums:
                    square_nums.remove(board[n*3 + 1][m*3 + 1])
                elif board[n*3 + 1][m*3 + 1] != ".":
                    return False
                
                if board[n*3 + 2][m*3 + 1] in square_nums:
                    square_nums.remove(board[n*3 + 2][m*3 + 1])
                elif board[n*3 + 2][m*3 + 1] != ".":
                    return False
                
                if board[n*3][m*3 + 2] in square_nums:
                    square_nums.remove(board[n*3][m*3 + 2])
                elif board[n*3][m*3 + 2] != ".":
                    return False
                
                if board[n*3 + 1][m*3 + 2] in square_nums:
                    square_nums.remove(board[n*3 + 1][m*3 + 2])
                elif board[n*3 + 1][m*3 + 2] != ".":
                    return False
                
                if board[n*3 + 2][m*3 + 2] in square_nums:
                    square_nums.remove(board[n*3 + 2][m*3 + 2])
                elif board[n*3 + 2][m*3 + 2] != ".":
                    return False
                
        return True
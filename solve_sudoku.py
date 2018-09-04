class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        return self.solve(board)

    def solve(self, board):
        for m in range(0, len(board)):
            for n in range(0, len(board[0])):
                if board[m][n] == '.':
                    for k in range(1, 10):
                        if self.isValidSudoku(m,n,str(k),board):
                            board[m][n] = str(k)
                            print board
                            print str(k)
                            print "------"
                            if self.solve(board):
                                return True
                            else:
                                board[m][n] = '.'
                    return False
        return True

    def isValidSudoku(self, row, col, c, board):
        print board
        for i in range(0, 9):
            if board[row][i] == c:
                print "row:{0}, col:{1}, c:{2}, crow:{3}, ccol:{4}".format(row, i, c, row, col)
                print "--------------------------------------"
                return False
            if board[i][col] == c:
                print "row:{0}, col:{1}, c:{2}, crow:{3}, ccol:{4}".format(i, col, c, row, col)
                print "--------------------------------------"
                return False
            if board[3*(row/3)+i/3][3*(col/3)+i%3] == c:
                return False

        return True


s = Solution()
sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(sudoku)
print sudoku
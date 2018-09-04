class Solution(object):
    def isValidSudoku(self, board):
        if not board:
            return False

        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board[0])):
                if not self.isValid(board[i][j], row) or not self.isValid(board[j][i], col):
                    return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                block = set()
                for k in range(0, 9):
                    item = board[i+k/3][j+k%3]
                    if not self.isValid(item, block):
                        return False

        return True


    def isValid(self, value, visited):
        if value == '.':
            return True
        v = ord(value) - ord('0')
        if v < 0 or v > 9 or value in visited:
            return False
        visited.add(value)
        return True
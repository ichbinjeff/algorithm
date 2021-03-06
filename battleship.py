class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                count += 1
        return count

s = Solution()
print s.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
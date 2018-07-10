class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if not board or not board[0]:
            return 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, word):
                    return True

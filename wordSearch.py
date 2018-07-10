class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        visited = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0] and self.search(board, word, "", i, j, visited):
                    return True
        return False
    
    def search(self, board, word, prev, i, j, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if (i,j) in visited:
            return False
        if len(prev) > len(word):
            return False
        visited.add((i,j))
        curr = prev + board[i][j]
        if word == curr:
            return True
        if self.search(board, word, curr, i+1, j, visited) or self.search(board, word, curr, i-1, j, visited) or self.search(board, word, curr, i, j-1, visited) or self.search(board, word, curr, i, j+1, visited):
            return True
        visited.remove((i, j))
        return False

s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
s.exist(board, "ABCCED")
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        rst = []
        direction = [[-1, 1], [1, -1]]
        row, col, d = 0, 0, 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                curr = matrix[i][j]
                row += direction[d][0]
                col += direction[d][1]

                if row >= len(matrix):
                    row = len(matrix) - 1
                    col += 2
                    d = 1 - d
                if col >= len(matrix[0]):
                    col = len(matrix[0])
                    row += 2
                    d = 1 - d
                if row < 0:
                    row = 0
                    d = 1 - d
                if col < 0:
                    col = 0
                    d = 1 - d
                rst.append(curr)
        return rst

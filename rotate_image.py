class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate_anticlock(self, matrix):
        for i in range(0, len(matrix)/2):
            for j in range(0, len(matrix[0])):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print matrix



s = Solution()
s.rotate_anticlock([[5,1,9,11], [2,4,8,10], [10,12,7,2], [6,3,14,3]])

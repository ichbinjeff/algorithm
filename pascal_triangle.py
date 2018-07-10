# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution(object):
    def generate(self, numRows):
        rst = []
        for i in range(0, numRows):
            level = [1] * (i+1)
            rst.append(level)
            if i > 1:
                for j in range(1, i):
                    rst[i][j] = rst[i-1][j] + rst[i-1][j-1]
        return rst

s = Solution()
print s.generate(4)
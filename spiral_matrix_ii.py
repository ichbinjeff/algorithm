class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rst = [[0 for i in range(n)] for i in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        curr = 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                rst[top][i] = curr
                curr += 1
            top += 1

            for i in range(top, bottom + 1):
                rst[i][right] = curr
                curr += 1
            right -= 1

            if left <= right:
                for i in range(right, left - 1, -1):
                    rst[bottom][i] = curr
                    curr += 1
                bottom -= 1

            if top <= bottom:
                for i in range(bottom, top - 1, -1):
                    rst[i][left] = curr
                    curr += 1
                left += 1
        return rst

# l=0
# r=2
# t=0
# b=2
#
# 0<=2 0<=2
# i in (0,3)
#     rst[0][0] = 1
#     curr = 2
#     rst[0][1] = 2
#     curr = 3
#     rst[0][2]=3
#     curr = 4
# top = 1
#
# i in (1,3)
#     rst(1)(2)=4
#     r(22)=5
# r = 1
# i in (1,-1)
#     r(2,1)=6
#     r(2,0)=7
# b = 1
#
# i in(1,0)
# r(1,0)=8
# left = 1
#
#
# 1<=1 1<=1
# i in (1,2)
# r(1,1)=9
# top = 2
#
# i in (2,2)
#
# i in(1,1)
# i in(1,1)
#

# 123
# 894
# 765
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return self.reverseN(-x) * (-1)
        return self.reverseN(x)

    # 12
    def reverseN(self, x):
        rst = 0
        while x > 0:
            rst = rst * 10 + x%10
            if rst >= 2 ** 31:
                return 0
            x /= 10
        return rst
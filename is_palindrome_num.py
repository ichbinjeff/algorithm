class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x%10 == 0):
            return False
        rst = 0
        while x > rst:
            rst = rst*10 + x%10
            x //= 10
        return x == rst or x == (rst//10)
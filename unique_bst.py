class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for level in range(2, n+1):
            for i in range(0, level):
                dp[level] += dp[i]*dp[level-i-1]
        return dp[n]

s = Solution()
print s.numTrees(5)
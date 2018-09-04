class Solution(object):
    def __init__(self):
        self.cache = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        first_match = False
        if s and (s[0] == p[0] or p[0] == '.'):
            first_match = True
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s[0:], p[2:]) or (first_match and self.isMatch(s[1:], p[0:]))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


    def isMatch_memo(self, s, p):
        memo = {}
        def search(i, j):
            print "({0}, {1})".format(i, j)
            if (i,j) in memo:
                return memo[i][j]
            if j == len(p):
                ans = i == len(s)
            else :
                firstMatch = False
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    firstMatch = True
                if j+1 < len(p) and p[j+1] == '*':
                    ans = search(i, j+2) or (firstMatch and search(i+1, j))
                else:
                    ans = firstMatch and search(i+1, j+1)
            memo[i,j] = ans
            return ans

        return search(0,0)

    def isMatch_cache(self, s, p):
        print self.cache
        if (s,p) in self.cache:
            return self.cache[(s,p)]

        if len(p) == 0:
            return len(s) == 0

        first_match = bool(s) and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            rout1 = self.isMatch_cache(s, p[2:])
            rout2 = first_match and self.isMatch_cache(s[1:], p)
            rst =  rout1 or rout2
            self.cache[(s,p)] = rst
            return rst
        else:
            rst = first_match and self.isMatch_cache(s[1:], p[1:])
            self.cache[(s,p)] = rst
            return rst

    def isMatch_dp(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j < len(p)-1 and p[j+1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]



s = Solution()
print s.isMatch_dp("ab", ".*c")
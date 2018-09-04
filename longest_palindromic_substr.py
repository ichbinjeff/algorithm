class Solution(object):
    #abcba
    def longest_palindromic(self, s):
        longest = s[0]
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                longest = s[i:i+2]

        for step in range(2, len(s)):
            for i in range(0, len(s)-step):
                dp[i][i + step] = dp[i + 1][i + step - 1] and s[i] == s[i + step]
                if dp[i][i + step]:
                    longest = s[i:i+step+1]

        return longest

s = Solution()
print s.longest_palindromic("abcba")
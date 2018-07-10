class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            print dp
            if dp[i-1]:
                if i - 1 + nums[i - 1] >= len(nums):
                    return True
                for j in range(i, i+nums[i-1]):
                    dp[j] = True
        return dp[len(nums) - 1]

s = Solution()
print s.canJump([3,0,8,2,0,0,1])
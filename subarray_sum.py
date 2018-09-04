class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        [23, 2, 4, 6, 7], k = 6
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if j-i >= 1:
                    if k != 0 and sum % k == 0:
                        return True
                    if sum == k:
                        return True
        return False
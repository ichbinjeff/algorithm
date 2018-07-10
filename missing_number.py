class Solution(object):
    # o(n) time and space
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])

        for i in range(0, len(nums)):
            if i not in num_set:
                return i

        return len(nums)

    # o(nlogn)
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    # o(n) o(1) space
    def missingNumber(self, nums):
        total_sum = sum(nums)
        expected_sum = (1 + len(nums)) * len(nums) / 2
        return expected_sum - total_sum

s = Solution()
print s.missingNumber([0,1,2,4])
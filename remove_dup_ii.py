class Solution(object):
    # 1113
    #11
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            nums[index] = nums[i]
            if i >= len(nums)-2 or (nums[i] != nums[i+1] or nums[i+1] != nums[i+2]):
                index += 1

        return index

s = Solution()
print s.removeDuplicates([1,1,1,2,2,2,3,3,3,3,4,4])
class Solution(object):
    # find first element smaller than curr item
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            nums.sort()
            return

        for j in range(len(nums) - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break

        start, end = i, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


s = Solution()
foo = [1,5,8,4,7,6,5,3,1]
s.nextPermutation(foo)
print foo
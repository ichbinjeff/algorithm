class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums)/2
        first_start, first_end, second_start, second_end = 0, mid, mid+1, len(nums)-1
        rst = []
        while first_start <= first_end and second_start <= second_end:
            rst.append(nums[first_end])
            first_end -= 1
            rst.append(nums[second_end])
            second_end -= 1


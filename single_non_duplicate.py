class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #11223
        #12233
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == nums[mid+1]:
                if (len(nums)-mid-1) % 2 == 0:
                    start = mid+1
                else:
                    end = mid
            else:
                if mid == 0 or nums[mid] != nums[mid-1]:
                    return nums[mid]
                if (len(nums)-mid-1) % 2 == 0:
                    end = mid
                else:
                    start = mid+1

        return nums[start]




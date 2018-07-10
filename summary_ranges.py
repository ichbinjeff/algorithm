class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # solution 1
        # if not nums:
        #     return []
        # ranges, rst = [], []
        # start, end = 0, 0
        # for i in range(1, len(nums) + 1):
        #     if i != len(nums) and nums[i - 1] + 1 == nums[i]:
        #         end = i
        #     else:
        #         if nums[start] == nums[end]:
        #             rst.append(str(nums[start]))
        #         else:
        #             rst.append(str(nums[start]) + "->" + str(nums[end]))
        #         start = i
        #         end = i
        #
        # return rst

        # solution 2
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([])

            ranges[-1][1:] = [n]
        print ranges
        return ['->'.join(map(str, r)) for r in ranges]

s = Solution()
print s.summaryRanges([0,1,2,4,5,7])
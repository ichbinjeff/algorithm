class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []
        level = []
        self._permute(rst, level, nums)
        return rst

    def _permute(self, rst, level, nums):
    	if len(level) == len(nums):
    		rst.append(level[:])
    		return
    	for i in range(0, len(nums)):
    		if nums[i] in level:
    			continue
    		level.append(nums[i])
    		self._permute(rst, level, nums)
    		level.pop()
    	
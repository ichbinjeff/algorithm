class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0

        max_val = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        right_max[len(height)-1]  = height[len(height)-1]

        for i in range(1, len(height)):
        	left_max[i] = max(height[i], left_max[i-1])

        for i in range(len(height)-2, -1, -1):
        	right_max[i] = max(height[i], right_max[i+1])

        for i in range(0, len(height)):
        	print "left: {0} right: {1} height: {2}".format(left_max, right_max, height[i])
        	max_val += min(left_max[i], right_max[i]) - height[i]
        return max_val


s = Solution()
print s.trap([2,0,2])

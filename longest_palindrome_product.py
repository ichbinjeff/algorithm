class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper_bound = 0
        while n > 0:
        	upper_bound = upper_bound * 10 + 9
        	n -= 1

        max_val = 0
    	lower_bound = upper_bound / 10 + 1
    	for i in range(upper_bound, lower_bound-1, -1):
    		for j in range(i, lower_bound-1, -1):
    			num = i * j
    			if self.is_palindrome(str(num)):
    				max_val = max(max_val, num)
    	return max_val % 1337

    def is_palindrome(self, value):
    	start, end = 0, len(value)-1
    	while start < end:
    		if value[start] != value[end]:
    			return False
    		start += 1
    		end -= 1
    	return True

s = Solution()
print s.largestPalindrome(3)
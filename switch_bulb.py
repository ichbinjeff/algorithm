import math

class Solution(object):
    def bulbSwitchMath(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

    #[0,0,0,0]
    def bulbSwitch(self, n):
        rst = [0] * (n+1)
        for step in range(1, n+1):
            for i in range(0, n+1, step):
                rst[i] = 1 - rst[i]
        return sum(rst[1:])

s = Solution()
print s.bulbSwitch(9)



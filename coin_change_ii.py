class Solution(object):
    def change(self, amount, coins, level):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        level += "-"
        ways = 0
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        for c in coins:
            way = self.change(amount-c, coins, level)
            print level + str(way)
            ways += way
        return ways

s = Solution()
print s.change(5, [1,2,5], "")
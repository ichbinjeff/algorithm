class Solution(object):
    def coinChange(self, coins, amount, cache):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in cache:
            return cache[amount]
        if amount == 0:
            return amount
        if amount < 0:
            return -1

        min_val = 2 ** 32
        for c in coins:
            candidate = self.coinChange(coins, amount-c, cache)
            if candidate != -1:
                min_val = min(min_val, candidate + 1)

        cache[amount] = min_val
        return -1 if min_val == 2 ** 32 else min_val

s = Solution()
print s.coinChange([1,2,5], 5, {})
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []
        path = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(rst, path, visited, nums, 0)
        return rst

    def dfs(self, rst, path, visited, nums, level):
        if len(path) == len(nums):
            rst.append(list(path))
            return

        for i in range(0, len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            path.append(nums[i])
            print "path: {0} set: {1} level: {2} index: {3}".format(path, visited, level, i)

            self.dfs(rst, path, visited, nums, level+1)
            path.pop()
            visited[i] = False


s = Solution()
print s.permuteUnique([2, 2, 1, 1])

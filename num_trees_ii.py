# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        curr_list = []
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        for i in range(start, end+1):
            left_nodes = self.dfs(start, i-1)
            right_nodes = self.dfs(i+1, end)
            for l in left_nodes:
                for r in right_nodes:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    curr_list.append(root)
        return curr_list

s = Solution()
print s.generateTrees(3)
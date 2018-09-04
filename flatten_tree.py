class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        root = self._flatten(root)

    def _flatten(self, root):
        if not root:
            return None
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.left = None
        root.right = left

        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right
        return root

s = Solution()
root = TreeNode(1)
two = TreeNode(2)
five = TreeNode(5)


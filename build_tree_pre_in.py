# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def _buildTree(self, preorder, prestart, preend, inorder, instart, inend):
        if prestart > preend or instart > inend or prestart < 0 or instart < 0:
            return None
        val = preorder[prestart]
        root = TreeNode(val)
        inorder_pos = self.find_inorder_pos(inorder, val)
        root.left = self._buildTree(preorder, prestart+1, preend, instart, inorder_pos-1)
        root.right = self._buildTree(preorder, prestart+2, preend, inorder_pos+1, inend)
        return root


    def find_inorder_pos(self, inorder, target):
        for i in range(0, len(inorder)):
            if inorder[i] == target:
                return i
        return -1

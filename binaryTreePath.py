class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        rst = []
        path = ""
        self.preorder(rst, root, path)
        return rst
    
    def preorder(self, rst, root, path):
        if not root:
            return
        if path != "":
            path += "->"
        path += str(root.val)
        if not root.left and not root.right:
            rst.append(path)
            return
        self.preorder(rst, root.left, path)
        self.preorder(rst, root.right, path)
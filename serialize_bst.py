# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder = self.preorder(root)
        inorder = sorted(preorder)
        return (preorder, inorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or len(data) != 2:
            return None
        preorder = data[0]
        inorder = data[1]
        return self.recover_tree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)


    def recover_tree(self, preorder, prestart, preend, inorder, instart, inend):
        if prestart > preend or instart > inend or prestart < 0 or instart < 0:
            return None
        val = preorder[prestart]
        if val == 3:
            print "prestarr:{0}, preend:{1}, instart:{2}, inend:{3}, root: {4}".format(prestart, preend, instart, inend, val)
        root = TreeNode(val)
        inorder_pos = self._find_in_pos(inorder, val)
        root.left = self.recover_tree(preorder, prestart+1, preend, inorder, inorder_pos-1, inend)
        root.right = self.recover_tree(preorder, prestart+2, preend, inorder, inorder_pos+1, inend)
        return root

    def preorder(self, root):
        if not root:
            return []
        curr = [root.val]
        curr.extend(self.preorder(root.left))
        curr.extend(self.preorder(root.right))
        return curr

    def _find_in_pos(self, inorder, val):
        for i in range(0, len(inorder)):
            if inorder[i] == val:
                return i
        return -1

# Your Codec object will be instantiated and called as such:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
codec = Codec()
root2 = codec.deserialize(codec.serialize(root))
print root2.val
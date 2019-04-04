# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        r = root
        while root.left or root.right:
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return r
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return r
        if root.val > val:
            root.left = TreeNode(val)
        else:
            root.right = TreeNode(val)
        return r

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        def helper(root, res):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                helper(root.left, res)
                helper(root.right, res)
        helper(root1, res1)
        helper(root2, res2)
        return True if res1 == res2 else False
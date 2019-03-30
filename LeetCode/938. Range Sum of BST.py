# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    range_sum = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def helper(root, L, R):
            if not root:
                return
            if L <= root.val <= R:
                self.range_sum += root.val
            helper(root.left, L, R)
            helper(root.right, L, R)

        helper(root, L, R)
        return self.range_sum
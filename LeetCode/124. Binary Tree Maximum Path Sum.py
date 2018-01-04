# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxValue = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxPathDown(node):
            if not node:
                return 0
            left = max(0, maxPathDown(node.left))
            right = max(0, maxPathDown(node.right))
            self.maxValue = max(self.maxValue, left + right + node.val)
            return max(left, right) + node.val

        maxPathDown(root)
        return self.maxValue

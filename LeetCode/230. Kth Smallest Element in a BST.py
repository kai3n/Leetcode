# Brute Force Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []

        def traversal(root):
            if root:
                traversal(root.left)
                res.append(root.val)
                traversal(root.right)

        traversal(root)
        return res[k - 1]

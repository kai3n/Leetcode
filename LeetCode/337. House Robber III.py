# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def robSub(root):
            if not root:
                return (0, 0)
            left = robSub(root.left)
            right = robSub(root.right)
            res = [0, 0]

            res[0] = max(left) + max(right)
            res[1] = root.val + left[0] + right[0]

            return res

        res = robSub(root)
        return max(res)

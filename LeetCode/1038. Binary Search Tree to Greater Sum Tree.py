# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        accu_sum = [0]
        def helper(root, accu_sum):
            if root:
                helper(root.right, accu_sum)
                accu_sum[0] += root.val
                root.val = accu_sum[0]
                helper(root.left, accu_sum)
        helper(root, accu_sum)
        return root


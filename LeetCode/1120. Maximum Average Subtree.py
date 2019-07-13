# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = 0
        def helper(root):
            if not root.left and not root.right:
                self.res = max(self.res, root.val)
                return 1, root.val
            left_num_of_node = 0
            left_total_sum = 0
            right_num_of_node = 0
            right_total_sum = 0
            if root.left:
                left_num_of_node, left_total_sum = helper(root.left)
            if root.right:
                right_num_of_node, right_total_sum = helper(root.right)
            n = left_num_of_node + right_num_of_node + 1
            v = left_total_sum + right_total_sum + root.val
            self.res = max(self.res, float(v)/float(n))
            return n, v
        helper(root)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = float('inf')
        self.node_list = []
        def helper(root):
            if root:
                helper(root.left)
                self.node_list.append(root.val)
                helper(root.right)
        helper(root)
        for i in range(1, len(self.node_list)):
            self.min_diff = min(abs(self.node_list[i-1]-self.node_list[i]), self.min_diff)
        return self.min_diff
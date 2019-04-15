# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root, val_min, val_max):
            if not root:
                return
            val_min = min(val_min, root.val)
            val_max = max(val_max, root.val)
            self.res = max(val_max-val_min, self.res)
            dfs(root.left, val_min, val_max)
            dfs(root.right, val_min, val_max)
        dfs(root, root.val, root.val)
        return self.res
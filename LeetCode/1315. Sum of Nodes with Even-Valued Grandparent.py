# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, parent, grand_parent):
            if node:
                if grand_parent and grand_parent.val % 2 == 0:
                    self.res += node.val
                dfs(node.left, node, parent)
                dfs(node.right, node, parent)
        dfs(root, None, None)
        return self.res

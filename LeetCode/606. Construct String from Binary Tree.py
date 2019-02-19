# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""

        ans = str(t.val)

        if t.left:
            ans += "(" + self.tree2str(t.left) + ")"

        if not t.left and t.right:
            ans += "()"

        if t.right:
            ans += "(" + self.tree2str(t.right) + ")"

        return ans
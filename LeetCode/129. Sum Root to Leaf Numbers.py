# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def helper(root, path, res):
            if root:
                if not root.left and not root.right:
                    res.append(path*10+root.val)
                else:
                    helper(root.left, path*10+root.val, res)
                    helper(root.right, path*10+root.val, res)
        helper(root, 0, res)
        return sum(res)
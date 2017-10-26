# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    closest = 0

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = root.val

        def helper(root, target):
            if root:
                if abs(target - root.val) < abs(target - self.closest):
                    self.closest = root.val
                if root.val > target:
                    helper(root.left, target)
                else:
                    helper(root.right, target)

        helper(root, target)
        return self.closest

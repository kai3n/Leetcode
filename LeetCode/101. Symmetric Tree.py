# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def isSymmetricHelp(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isSymmetricHelp(left.left, right.right) and isSymmetricHelp(left.right, right.left)
        return isSymmetricHelp(root.left, root.right) if root is not None else True


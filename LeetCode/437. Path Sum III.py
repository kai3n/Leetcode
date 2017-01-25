# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumUp(self, root, pre, sum):
        if root is None:
            return 0
        cur = pre + root.val
        return (cur == sum) + self.sumUp(root.left, cur, sum) + self.sumUp(root.right, cur, sum)

    def pathSum(self, root, sum):
        if root is None:
            return 0
        return self.sumUp(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

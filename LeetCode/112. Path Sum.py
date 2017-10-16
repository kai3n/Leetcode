# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(root, pathSum, sum):
    if root:
        pathSum += root.val
        if root.left == None and root.right == None and pathSum == sum:
            return True
        else:
            return helper(root.left, pathSum, sum) or helper(root.right, pathSum, sum)
    return False


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            return helper(root, 0, sum)
        return False

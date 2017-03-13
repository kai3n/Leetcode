# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []
        row = [root]
        while any(row):
            tmp = []
            maxes.append(max(node.val for node in row))
            for node in row:
                for kid in (node.left, node.right):
                    if kid:
                        tmp.append(kid)
            row = tmp
        return maxes
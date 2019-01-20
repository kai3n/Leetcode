# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def surplus(node):
            nonlocal moves
            if node is None:
                return 0
            l, r = surplus(node.left), surplus(node.right)
            moves += abs(l) + abs(r)
            return node.val + l + r - 1

        moves = 0
        surplus(root)
        return moves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traversal(root):
            if root:
                self.count += 1
                traversal(root.left)
                traversal(root.right)

        traversal(root)
        return self.count
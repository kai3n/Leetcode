# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        beg = 1
        max_width = 1
        depth = 0
        index = 1
        queue = [[root, depth, index]]

        while queue:
            n, d, i = queue.pop(0)
            if d != depth:
                depth = d
                beg = i
            max_width = max(max_width, i - beg + 1)
            if n.left:
                queue.append([n.left, d + 1, i * 2])
            if n.right:
                queue.append([n.right, d + 1, i * 2 + 1])

        return max_width

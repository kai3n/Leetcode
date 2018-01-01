# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        depth = 0
        queue = [[root, depth]]
        res = []
        each = []

        while queue:
            n, d = queue.pop(0)
            if depth != d:
                depth += 1
                res.append(each)
                each = [n.val]
            else:
                each.append(n.val)
            for c in [n.left, n.right]:
                if c is not None:
                    queue.append([c, d + 1])
        res.append(each)
        return res

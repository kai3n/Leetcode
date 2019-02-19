# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    p = d = -1
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def helper(curr, parent, depth, n):
            if curr:
                if curr.val == n:
                    self.p = parent
                    self.d = depth
                helper(curr.left, curr, depth+1, n)
                helper(curr.right, curr, depth+1, n)
        helper(root, None, 0, x)
        p1, d1 = self.p, self.d
        helper(root, None, 0, y)
        p2, d2 = self.p, self.d
        if d1 != -1 and d2 != -1 and d1 == d2 and p1 != p2:
            return True
        return False

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        d = {}

        def traverse(root, par=None, depth=0):
            if root and (x not in d or y not in d):
                d[root.val] = (depth, par)
                traverse(root.left, root, depth + 1)
                traverse(root.right, root, depth + 1)

        traverse(root)
        return d[x][0] == d[y][0] and d[x][1] != d[y][1]
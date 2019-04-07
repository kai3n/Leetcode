# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        stack = [[root, [root.val]]]
        while stack:
            n, p = stack.pop()
            if not n.left and not n.right:
                print(p)
                res += int(''.join(map(str, p)), 2)
            if n.left:
                stack.append([n.left, p + [n.left.val]])
            if n.right:
                stack.append([n.right, p + [n.right.val]])

        return res
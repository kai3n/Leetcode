# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        l = []

        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)

        inorder(root)

        left = 0
        right = len(l) - 1

        while left < right:
            if l[left] + l[right] == k:
                return True
            elif l[left] + l[right] > k:
                right -= 1
            else:
                left += 1
        return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def postorder(root, parent):
            if root:
                left = postorder(root.left, root)
                right = postorder(root.right, root)
                root.left = left
                root.right = right
                if not root.left and not root.right:
                    if root.val == target:
                        return None
                return root
        return postorder(root, None)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)

        inorder(root)

        def build_tree(arr):
            if not arr:
                return None
            i = len(arr) // 2
            root = TreeNode(arr[i])
            root.left = build_tree(arr[:i])
            root.right = build_tree(arr[i + 1:])
            return root

        return build_tree(arr)

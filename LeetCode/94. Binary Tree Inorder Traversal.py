# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right

        return ans
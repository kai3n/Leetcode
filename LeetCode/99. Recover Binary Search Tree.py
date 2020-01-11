# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prevNode = TreeNode(float('-inf'))
        self.first, self.second = None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if not self.first and self.prevNode.val > root.val:
                self.first, self.second = self.prevNode, root
            if self.first and self.prevNode.val > root.val:
                self.second = root
            self.prevNode = root
            self.inorder(root.right)
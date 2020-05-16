# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def helper(root, max_val):
            if root:
                if root.val >= max_val:
                    self.count += 1
                helper(root.left, max(root.val, max_val))
                helper(root.right, max(root.val, max_val))
        helper(root, float('-inf'))
        return self.count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
    
        def helper(node):
            if not node:
                return None
            if node in nodes:
                return node

            left = helper(node.left)
            right = helper(node.right)
            
            if left and right:
                return node
            return left or right
        return helper(root)

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        def helper(node, prev):
            if not node:
                return None
            if node == root:
                node.parent = prev
                return node
            if node.left:
                node.right = node.left
            if node.parent.left == node:
                node.parent.left = None
            if node.parent.right == node:
                node.parent.right = None
            node.left = helper(node.parent, node)
            node.parent = prev
            return node
        return helper(leaf, None)

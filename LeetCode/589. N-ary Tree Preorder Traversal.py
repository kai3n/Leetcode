"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []

        def helper(root):
            if root:
                self.res.append(root.val)
                for child in root.children:
                    helper(child)

        helper(root)
        return self.res

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                cur.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(cur)
        return res

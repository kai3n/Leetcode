"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue = [root]
        res = []
        while queue:
            l = len(queue)
            group = []
            for _ in range(l):
                node = queue.pop(0)
                group.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(group[:])

        for i in range(len(res)):
            if len(res[i]) == 1:
                continue
            for j in range(len(res[i]) - 1):
                res[i][j].next = res[i][j + 1]
        return root

    def connect(self, node):
        tail = dummy = TreeLinkNode(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
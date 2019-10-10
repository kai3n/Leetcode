"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        new_node = Node(insertVal, head)

        if not head:
            return new_node

        node = head
        while True:
            if node.next.val < node.val and (insertVal <= node.next.val or insertVal >= node.val):
                break
            elif node.val <= insertVal <= node.next.val:
                break
            elif node.next == head:
                break
            node = node.next

        new_node.next = node.next
        node.next = new_node
        return head
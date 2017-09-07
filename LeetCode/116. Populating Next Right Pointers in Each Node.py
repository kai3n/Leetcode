# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        queue = []
        depth = -1
        if root:
            queue.append([root, depth+1])

        while queue:
            node, d = queue.pop(0)
            if d - depth == 1:
                prev = node
            else:
                node.next = prev
                prev = node
            depth = d

            for child in [node.right, node.left]:
                if child:
                    queue.append([child, d+1])
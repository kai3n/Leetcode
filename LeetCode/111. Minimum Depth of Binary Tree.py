# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root:
            depth = 1
            q = [(root,depth)]
            while len(q) > 0:
                n, d = q.pop(0)
                if n.left or n.right:
                    if n.left is not None:
                        q.append((n.left,d+1))
                    if n.right is not None:
                        q.append((n.right,d+1))
                else:
                    return d
        return depth




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        def bfs(root, depth):

            queue = [[root, depth]]
            while queue:
                n, d = queue.pop(0)
                if len(res) == d:
                    res.append([n.val])
                else:
                    res[d].append(n.val)

                if n.left:
                    queue.append([n.left, d + 1])
                if n.right:
                    queue.append([n.right, d + 1])

        bfs(root, 0)

        for i in range(len(res)):
            if i & 1:
                res[i] = res[i][::-1]
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = []
        visited = set()
        visited.add(1)

        def dfs(root, path, v):
            if root:
                if not root.left and not root.right:
                    res.append([root.val] + path)
                    return
                if v * 2 not in visited:
                    visited.add(v * 2)
                    dfs(root.left, [root.val] + path, v * 2)
                if v * 2 + 1 not in visited:
                    visited.add(v * 2 + 1)
                    dfs(root.right, [root.val] + path, v * 2 + 1)

        dfs(root, [], 1)
        return "".join(map(lambda x: chr(97 + x), sorted(res)[0]))


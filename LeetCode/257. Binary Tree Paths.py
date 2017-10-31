# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []

        def dfs(root, path):
            if root:
                path += "->" + str(root.val)
                if not root.left and not root.right:
                    paths.append(path[2:])
                if root.left:
                    dfs(root.left, path)
                if root.right:
                    dfs(root.right, path)

        dfs(root, "")
        return paths


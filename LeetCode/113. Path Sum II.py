# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.r = []
        if root is None:
            return self.r

        def dfs(root, subSum, path):
            if root.left:
                dfs(root.left, subSum + root.val, path + [root.val])
            if root.right:
                dfs(root.right, subSum + root.val, path + [root.val])
            if subSum + root.val == sum and not root.left and not root.right:
                self.r += [path + [root.val]]

        dfs(root, 0, [])
        return self.r

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
test = Solution()
print(test.pathSum(root, 12))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution(object):

    def helper(self, root, target):
        if root:
            if root == target:
                return True
            return self.helper(root.left, target) or self.helper(root.right, target)
        return False

    def lowestCommonAncestor(self, root, p, q):

        while root:
            if self.helper(p, q):
                return p
            if self.helper(q, p):
                return q
            if self.helper(root.left, p) and self.helper(root.left, q):
                root = root.left
            if self.helper(root.right, p) and self.helper(root.right, q):
                root = root.right
            else:
                return root

node = TreeNode(2)
node.right = TreeNode(1)
# node.right = TreeNode(4)
# node.right.left = TreeNode(6)



test = Solution()
print(test.lowestCommonAncestor(node, node, node.right))
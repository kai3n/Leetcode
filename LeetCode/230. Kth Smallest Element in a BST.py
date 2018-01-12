# Brute Force Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []

        def traversal(root):
            if root:
                traversal(root.left)
                res.append(root.val)
                traversal(root.right)

        traversal(root)
        return res[k - 1]

# Recursive

def kthSmallest(self, root, k):
    self.k = k
    self.res = None
    self.helper(root)
    return self.res

def helper(self, node):
    if not node:
        return
    self.helper(node.left)
    self.k -= 1
    if self.k == 0:
        self.res = node.val
        return
    self.helper(node.right)

# Iterative
def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
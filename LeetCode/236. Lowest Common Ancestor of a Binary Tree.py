# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(root, v):
    if root:
        if root.val == v:
            return True
        return helper(root.left, v) or helper(root.right, v)
    return False



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root:
            if root.val == p and (helper(root.left, q) or helper(root.right, q)):
                return root
            elif root.val == q and (helper(root.left, p) or helper(root.right, p)):
                return root
            elif helper(root.left, p) and helper(root.right, q):
                return root
            elif helper(root.left, q) and helper(root.right, p):
                return root
            l = self.lowestCommonAncestor(root.left, p, q)
            if l != -1:
                return l
            r = self.lowestCommonAncestor(root.right, p, q)
            if r != -1:
                return r
        return -1

node = TreeNode(2)
node.right = TreeNode(1)
# node.right = TreeNode(4)
# node.right.left = TreeNode(6)

print(helper(node, 7))

test = Solution()
print(test.lowestCommonAncestor(node, 1, 2).val)
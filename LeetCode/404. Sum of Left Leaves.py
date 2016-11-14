class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumLeftLeaves(rt, is_left=False):
            if rt is None or (rt.left is None and rt.right is None and is_left is False):
                return 0
            elif rt.left is None and rt.right is None and is_left is True:
                return rt.val
            else:
                return sumLeftLeaves(rt.left, True) + sumLeftLeaves(rt.right, False)

        return sumLeftLeaves(root)

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right= TreeNode(20)
tree.right.left = TreeNode(20)
tree.right.right = TreeNode(20)
test = Solution()
print(test.sumOfLeftLeaves(tree))



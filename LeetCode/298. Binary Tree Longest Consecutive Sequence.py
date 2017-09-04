# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        res = 0
        while len(stack):
            node, length = stack.pop()
            res = max(res, length)
            for child in [node.left, node.right]:
                if child:
                    l = length+1 if child.val == node.val+1 else 1
                    stack.append(child, l)
        return res

test = Solution()
test.longestConsecutive(TreeNode(10))


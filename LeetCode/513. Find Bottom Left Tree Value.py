# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height = 0
        self.depth = 0
        self.highestNode = []

        def findHeight(root, depth):
            if self.height < depth:
                self.height = depth
            if root.left:
                findHeight(root.left, depth + 1)
            if root.right:
                findHeight(root.right, depth + 1)

        def findHighestNode(root, depth):
            if self.height == depth:
                self.highestNode.append(root)
            if root.left:
                findHighestNode(root.left, depth + 1)
            if root.right:
                findHighestNode(root.right, depth + 1)

        findHeight(root, self.depth)
        findHighestNode(root, self.depth)
        return self.highestNode[0].val

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

test = Solution()
print(test.findBottomLeftValue(root))


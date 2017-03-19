# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
#         self.minHeight = 999999
#         self.maxHeight = 0
#         def inOrder(root, height):
#             if root.left:
#                 inOrder(root.left, height+1)
#             else:
#                 if self.minHeight > height:
#                     self.minHeight = height
#                 if self.maxHeight < height:
#                     self.maxHeight = height
#             if root.right:
#                 inOrder(root.right, height+1)
#             else:
#                 if self.minHeight > height:
#                     self.minHeight = height
#                 if self.maxHeight < height:
#                     self.maxHeight = height
#         inOrder(root, 1)
#         if self.maxHeight - self.minHeight > 1:
#             return False
#         else:
#             return True

class Solution(object):
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)

root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.left.left = TreeNode(7)

root3 = None

test = Solution()
print(test.isBalanced(root))
print(test.isBalanced(root2))
print(test.isBalanced(root3))
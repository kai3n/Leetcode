# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        totalRes = []
        if root:
            def postorder(root):
                if root:
                    if (root.left is None and root.right is None):
                        if root.val != '*':
                            eachRes.append(root.val)
                            root.val = '*'
                    elif root.left and root.left.val == '*' and root.right and root.right.val == '*':
                        if root.val != '*':
                            eachRes.append(root.val)
                            root.val = '*'
                    elif root.left and root.left.val == '*' and root.right is None:
                        if root.val != '*':
                            eachRes.append(root.val)
                            root.val = '*'
                    elif root.right and root.right.val == '*' and root.left is None:
                        if root.val != '*':
                            eachRes.append(root.val)
                            root.val = '*'
                    postorder(root.left)
                    postorder(root.right)


            while root.val != '*':
                eachRes = []
                postorder(root)
                totalRes.append(eachRes)
        return totalRes

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

test = Solution()
print(test.findLeaves(root))



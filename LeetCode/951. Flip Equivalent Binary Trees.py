# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def helper(root1, root2):
            if root1 and root2:
                if root1.val != root2.val:
                    return False

                if root1.left and root2.left and root1.right and root2.right:
                    if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
                        return helper(root1.left, root2.left) and helper(root1.right, root2.right)
                    elif root1.left.val == root2.right.val and root1.right.val == root2.left.val:
                        return helper(root1.left, root2.right) and helper(root1.right, root2.left)
                    else:
                        return False
                elif not root1.left and not root2.left and root1.right and root2.right:
                    if root1.right.val == root2.right.val:
                        return helper(root1.right, root2.right)
                    else:
                        return False
                elif root1.left and root2.left and not root1.right and not root2.right:
                    if root1.left.val == root2.left.val:
                        return helper(root1.left, root2.left)
                    else:
                        return False
                elif root1.left and not root2.left and not root1.right and root2.right:
                    if root1.left.val == root2.right.val:
                        return helper(root1.left, root2.right)
                    else:
                        return False
                elif not root1.left and root2.left and root1.right and not root2.right:
                    if root1.right.val == root2.left.val:
                        return helper(root1.right, root2.left)
                    else:
                        return False
                elif not root1.left and not root2.left and not root1.right and not root2.right:
                    return True
                else:
                    return False
            elif root1 and not root2:
                return False
            elif not root1 and root2:
                return False
            return True

        return helper(root1, root2)
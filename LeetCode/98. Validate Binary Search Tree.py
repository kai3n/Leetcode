# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        self.arr =[]
        if not root:
            return
        if root.left is None and root.right is None:
            return True
        def helper(root):
            if root:
                helper(root.left)
                self.arr.append(root.val)
                helper(root.right)
        helper(root)
        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True


class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

class Solution:
    def isSame(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
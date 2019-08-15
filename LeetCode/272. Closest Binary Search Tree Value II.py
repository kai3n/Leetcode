# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.l = []
        def helper(root):
            if root:
                helper(root.left)
                self.l.append(root.val)
                helper(root.right)
        helper(root)
        res = []
        p = len(self.l)
        for i in range(len(self.l)):
            if self.l[i] > target:
                self.l.insert(i, target)
                p = i
                break
        l = p-1
        r = p+1
        i = 0
        while i < k:
            if 0 <= l < len(self.l) and 0 <= r < len(self.l):
                if abs(target-self.l[l]) < abs(target-self.l[r]):
                    res.append(self.l[l])
                    l -= 1
                else:
                    res.append(self.l[r])
                    r += 1
            elif 0 <= l < len(self.l):
                res.append(self.l[l])
                l -= 1
            elif 0 <= r < len(self.l):
                res.append(self.l[r])
                r += 1
            i += 1
        return res
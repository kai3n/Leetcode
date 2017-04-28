# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []

        def getSum(node):
            if node == None: return 0
            s = node.val + getSum(node.left) + getSum(node.right)
            c[s] += 1
            return s

        from collections import Counter
        c = Counter()
        getSum(root)
        frequent = max(c.values())
        return [s for s in c.keys() if c[s] == frequent]
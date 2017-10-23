class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import Counter
        count = Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_count = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_count]
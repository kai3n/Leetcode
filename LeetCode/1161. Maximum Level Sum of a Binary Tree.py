# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        depth = 1
        max_sum = float('-inf')
        max_depth = 1
        while queue:
            l = len(queue)
            level_sum = 0
            for _ in range(l):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(level_sum)
            if max_sum < level_sum:
                max_sum = level_sum
                max_depth = depth
            depth += 1
        return max_depth


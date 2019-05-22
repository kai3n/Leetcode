# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        if len(pre) ==2:
            root = TreeNode(pre[0])
            root.left = TreeNode(pre[1])
            return root
        root = TreeNode(pre[0])
        split_index = -1
        for i in range(1, len(pre)):
            if set(pre[1:i+1]) == set(post[:i]):
                split_index = i
                break
        root.left = self.constructFromPrePost(pre[1:split_index+1], post[:split_index])
        root.right = self.constructFromPrePost(pre[split_index+1:], post[split_index:-1])
        return root
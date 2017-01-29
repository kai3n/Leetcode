# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeDic = dict()
        def travesal(root):
            if root.left:
                travesal(root.left)
            if nodeDic.get(root.val) is None:
                nodeDic[root.val] = 1
            else:
                nodeDic[root.val] += 1
            if root.right:
                travesal(root.right)
        travesal(root)
        maxCnt = max(nodeDic.items(), key=lambda x:x[1])[1]
        return [i[0] for i in nodeDic.items() if i[1] == maxCnt]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        depth = 0
        queue = []
        layerAvgList = []
        queue.append((root, depth))

        while len(queue) != 0:
            node, curDepth = queue.pop(0)

            if len(layerAvgList) <= curDepth:
                layerAvgList.append([node.val])
            else:
                layerAvgList[curDepth].append(node.val)

            if node.left:
                queue.append((node.left, curDepth+1))
            if node.right:
                queue.append((node.right, curDepth+1))

        output = []
        for i in layerAvgList:
            output.append(float(sum(i))/float(len(i)))
        return output
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.list1 = []
        self.list2 = []
        self.res = []
        i = j = 0
        def inorder(root, l):
            if root:
                inorder(root.left, l)
                l.append(root.val)
                inorder(root.right, l)
        inorder(root1, self.list1)
        inorder(root2, self.list2)
        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] <= self.list2[j]:
                self.res.append(self.list1[i])
                i += 1
            else:
                self.res.append(self.list2[j])
                j += 1
        while i < len(self.list1):
            self.res.append(self.list1[i])
            i += 1
        while j < len(self.list2):
            self.res.append(self.list2[j])
            j += 1
        return self.res
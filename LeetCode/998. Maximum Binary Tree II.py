# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        A = []
        def inorder(root):
            if root:
                inorder(root.left)
                A.append(root.val)
                inorder(root.right)
        inorder(root)
        print(A)
        B = A + [val]
        print(B)
        def build_tree(arr):
            if arr:
                max_val = max(arr)
                index = arr.index(max_val)
                left_arr = arr[:index]
                right_arr = arr[index+1:]
                root = TreeNode(max_val)
                root.left = build_tree(left_arr)
                root.right = build_tree(right_arr)
                return root
        return build_tree(B)
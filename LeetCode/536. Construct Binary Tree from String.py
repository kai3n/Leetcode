# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, S):
        ix = S.find('(')
        if ix < 0:
            return TreeNode(int(S)) if S else None

        bal = 0
        for jx, u in enumerate(S):
            if u == '(': bal += 1
            if u == ')': bal -= 1
            if jx > ix and bal == 0:
                break

        root = TreeNode(int(S[:ix]))
        root.left = self.str2tree(S[ix+1:jx])
        root.right = self.str2tree(S[jx+2:-1])
        return root

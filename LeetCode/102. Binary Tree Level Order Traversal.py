# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def levelOrder(self, root):
    if not root:
        return []
    queue = [[root, 0]]
    res = []
    while queue:
        node, depth = queue.pop(0)
        if depth < len(res):
            res[depth].append(node.val)
        else:
            res.append([node.val])
        for c in [node.left, node.right]:
            if c is not None:
                queue.append([c, depth + 1])
    return res



# Another Solution
def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans

# Another Solution2

class Solution(object):
    def __init__(self):
        self.l=[]
    def helper(self,root,level):
        if not root:
            return None
        else:
            if level<len(self.l):
                self.l[level].append(root.val)
            else:
                self.l.append([root.val])
            self.helper(root.left,level+1)
            self.helper(root.right,level+1)
        return self.l
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.helper(root,0)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        q = []
        q.append(root)
        while q:
            q_size = len(q)
            l_by_lvl = []
            for i in range(q_size):
                child = q.pop(0)
                l_by_lvl.append(child.val)
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
            res.append(l_by_lvl)
        return res

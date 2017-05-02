# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            nodes.append(root.val)
            if root.right:
                inorder(root.right)

        def convertBST(root):
            if root.left:
                convertBST(root.left)
            root.val = sum(nodes[nodes.index(root.val):])
            if root.right:
                convertBST(root.right)

        inorder(root)
        nodes = sorted(nodes)
        convertBST(root)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

test = Solution()
test.convertBST(root)

"""
public TreeNode convertBST(TreeNode root) {
    dfs(root, 0);
    return root;
}
public int dfs(TreeNode root, int val) {
    if(root == null) return val;
    int right = dfs(root.right, val);
    int left = dfs(root.left, root.val + right);
    root.val = root.val + right;
    return left;
}
"""
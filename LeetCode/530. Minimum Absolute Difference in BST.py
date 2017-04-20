# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valueList = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            valueList.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        minimum = sum(valueList)
        valueList = sorted(valueList)
        for i in range(1, len(valueList)):
            if valueList[i] - valueList[i-1] < minimum:
                minimum = valueList[i] - valueList[i-1]
        return minimum

# root = TreeNode(10)
# root.left = None
# root.right = TreeNode(30)
# root.right.left = TreeNode(23)
# root.right.right = TreeNode(84)

root = TreeNode(1)
root.left = None
root.right = TreeNode(5)
root.right.left = TreeNode(3)


test = Solution()
print(test.getMinimumDifference(root))



"""
public class Solution {
    int min = Integer.MAX_VALUE;
    Integer prev = null;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;

        getMinimumDifference(root.left);

        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;

        getMinimumDifference(root.right);

        return min;
    }

}
"""
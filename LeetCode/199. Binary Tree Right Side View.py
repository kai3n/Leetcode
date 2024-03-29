# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lvl = 0
        queue = [[root, lvl]]
        prev = root
        res = []

        while queue:
            node, level = queue.pop(0)

            if level != lvl:
                res.append(prev.val)
                lvl = level
            if root:
                if node.left:
                    queue.append([node.left, level + 1])
                if node.right:
                    queue.append([node.right, level + 1])
            prev = node
        if node:
            res.append(node.val)
        return res


# Another Solution
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        ans=[root.val]
        left=ans+self.rightSideView(root.left)
        right=ans+self.rightSideView(root.right)
        if len(right)>=len(left):
            return right
        return right+left[len(right):]

"""
//Good Java Solution

public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        rightView(root, result, 0);
        return result;
    }
    
    public void rightView(TreeNode curr, List<Integer> result, int currDepth){
        if(curr == null){
            return;
        }
        if(currDepth == result.size()){
            result.add(curr.val);
        }
        
        rightView(curr.right, result, currDepth + 1);
        rightView(curr.left, result, currDepth + 1);
        
    }
}
"""
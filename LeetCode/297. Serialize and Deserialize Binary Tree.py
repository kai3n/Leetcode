"""
    1
   / \
  2   3
     / \
    4   5

[0, 1, 2, 3, -1, -1, 4, 5]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.max_depth = 0
        def inorder(root, depth):
            if root:
                inorder(root.left, depth + 1)
                self.max_depth = max(self.max_depth, depth)
                inorder(root.right, depth + 1)

        def preorder(root, index):
            if root:
                self.arr[index] = root.val
                preorder(root.left, index*2)
                preorder(root.right, index*2+1)
        inorder(root, 1)
        self.arr = [-1 for _ in range(2 ** self.max_depth)]
        preorder(root, 1)
        return self.arr


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(data, index):
            if data[index] != -1 and index < len(data):
                root = TreeNode(data[index])
                if index * 2 < len(data):
                    root.left = helper(data, index * 2)
                if index * 2 + 1< len(data):
                    root.right = helper(data, index * 2 + 1)
                return root

        return helper(data, 1)


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
print(codec.serialize(root))
root = codec.deserialize(codec.serialize(root))
print(root)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return []

        if not root.children:
            return root.val

        return [
            root.val,
            [self.serialize(c) for c in root.children]
        ]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == []:
            return None

        # Handle leaf node case when the data is an int instead of list
        if isinstance(data, int):
            return Node(data, [])

        return Node(
            val=data[0],
            children=[self.deserialize(c) for c in data[1]]
        )

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
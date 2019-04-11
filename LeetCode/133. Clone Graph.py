"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node', memo={}) -> 'Node':
        if node in memo:
            return memo[node]
        if not node:
            return None
        root = Node(node.val, [])
        memo[node] = root
        for nei in node.neighbors:
            root.neighbors.append(self.cloneGraph(nei))
        return root
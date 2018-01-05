# Cheat Key
class MapSum(object):

    def __init__(self):
        self.d = {}

    def insert(self, key, val):
        self.d[key] = val

    def sum(self, prefix):
        return sum(self.d[i] for i in self.d if i.startswith(prefix))

# Right Solution

class TrieNode():
    def __init__(self, count=0):
        self.count = count
        self.children = {}


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # Time: O(k)
        curr = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        curr = self.root
        curr.count += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # Time: O(k)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count
class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution(object):
    def alienOrder(self, words):
        # find out nodes
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = Node()

        # find out directed edges (from StefanPochmann)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    graph[a].OUT.add(b)
                    graph[b].IN.add(a)
                    break

        # topo-sort
        res = ""
        while graph:
            oldlen = len(graph)

            for key in graph:
                if not graph[key].IN:   # to remove this
                    for key2 in graph[key].OUT:
                        graph[key2].IN.remove(key)
                    del graph[key]
                    res += key
                    break

            if oldlen == len(graph): # if shrinking stops, solution doesn't exist
                return ""
            oldlen = len(graph)
        return res
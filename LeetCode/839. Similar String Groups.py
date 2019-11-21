class Solution:
    def numSimilarGroups(self, a):
        n = len(a)
        ufind = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if self.is_similar(a[i], a[j]):
                    ufind.union(i, j)
        return ufind.get_num_groups()
    def is_similar(self, a, b):
         return len(list(filter(lambda i: a[i] != b[i], range(len(a))))) in (0, 2)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

    def get_num_groups(self):
        return sum([1 for i in range(len(self.parent)) if i == self.parent[i]])
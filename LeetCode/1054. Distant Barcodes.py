class Solution(object):
    def rearrangeBarcodes(self, packages):
        i, n = 0, len(packages)
        res = [0] * n
        for k, v in collections.Counter(packages).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res
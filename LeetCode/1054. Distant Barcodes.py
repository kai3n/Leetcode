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

class Solution(object):
    def rearrangeBarcodes(self, A):
        count = collections.Counter(A)
        A.sort(key=lambda a: (count[a], a))
        A[1::2], A[::2] = A[0:len(A) / 2], A[len(A) / 2:]
        return A
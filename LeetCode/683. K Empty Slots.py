class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        tree = [0] * (len(flowers) + 1)
        maxVal = len(flowers)

        def update(idx, val):
            while idx <= maxVal:
                tree[idx] += val
                idx += (idx & -idx)

        def read(idx):
            sum = 0
            while idx > 0:
                sum += tree[idx]
                idx -= (idx & -idx)
            return sum

        d = dict()
        for i, v in enumerate(flowers):
            update(v, 1)
            if v - k - 1 in d:
                if read(v) - read(v - k - 1) == 1:
                    return i + 1
            if v + k + 1 in d:
                if read(v + k + 1) - read(v) == 1:
                    return i + 1
            d[v] = True
        return -1
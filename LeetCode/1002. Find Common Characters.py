class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict

        d = defaultdict(int)

        for letter in A[0]:
            d[letter] += 1

        for word in A[1:]:
            new_d = defaultdict(int)
            for letter in word:
                new_d[letter] += 1
            for k, v in new_d.items():
                if d.get(k) is not None:
                    new_d[k] = min(v, d[k])
                else:
                    del new_d[k]
            d = new_d
        res = []
        for k, v in d.items():
            for _ in range(v):
                res.append(k)
        return res
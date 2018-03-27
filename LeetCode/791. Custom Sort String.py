class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {k: i for i, k in enumerate(S)}

        def compare(x, y):
            return (d.get(x, -1) > d.get(y, -1)) - (d.get(y, -1) > d.get(x, -1))

        res = sorted(T, cmp=compare)

        print(res)
        return ''.join(res)
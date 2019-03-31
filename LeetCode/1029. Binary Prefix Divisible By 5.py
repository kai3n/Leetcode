class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        total_sum = 0
        res = []
        for i, e in enumerate(A):
            total_sum = total_sum*2+e
            if total_sum % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
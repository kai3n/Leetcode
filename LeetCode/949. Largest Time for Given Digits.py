class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        res = []

        def helper(A, p):
            if len(p) == 4:
                if p[0] == 2 and 0 <= p[1] <= 3 and 0 <= p[2] <= 5:
                    res.append(p)
                elif p[0] == 1 and 0 <= p[1] <= 9 and 0 <= p[2] <= 5:
                    res.append(p)
                elif p[0] == 0 and 0 <= p[1] <= 9 and 0 <= p[2] <= 5:
                    res.append(p)
            for i in range(len(A)):
                helper(A[:i] + A[i + 1:], p + [A[i]])

        helper(A, [])
        if not res:
            return ""
        max_time = max(res)
        return str(max_time[0]) + str(max_time[1]) + ":" + str(max_time[2]) + str(max_time[3])

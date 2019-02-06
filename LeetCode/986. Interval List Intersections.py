# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        a = 0
        b = 0
        res = []
        while a < len(A) and b < len(B):
            if A[a].start > B[b].start:
                if B[b].end < A[a].start:
                    b += 1
                elif A[a].end > B[b].end:
                    res.append(Interval(A[a].start, B[b].end))
                    b += 1
                else:
                    res.append(Interval(A[a].start, A[a].end))
                    a += 1
            else:
                if A[a].end < B[b].start:
                    a += 1
                elif A[a].end < B[b].end:
                    res.append(Interval(B[b].start, A[a].end))
                    a += 1
                else:
                    res.append(Interval(B[b].start, B[b].end))
                    b += 1
        return res
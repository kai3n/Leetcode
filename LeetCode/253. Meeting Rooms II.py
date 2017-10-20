# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda i:i.start)
        pq= []
        res = 0
        for i in intervals:

            while pq and pq[0] <= i.start:
                heappop(pq)
            heappush(pq, i.end)
            res = max(res, len(pq))
        return res

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x.start)
        intervals.append(Interval(9999999999999,99999999999999))
        res = []
        begin = intervals[0].start
        end = intervals[0].end
        i = 1
        while i < len(intervals):
            while i < len(intervals) and intervals[i].start <= end:
                end = max(end, intervals[i].end)
                i += 1
            res.append([begin, end])
            if i < len(intervals):
                begin = intervals[i].start
                end = intervals[i].end
            i += 1
        return res

a = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
a = [Interval(1,4),Interval(2,3)]
a = [Interval(1,4),Interval(4,5)]
test = Solution()
print(test.merge(a))


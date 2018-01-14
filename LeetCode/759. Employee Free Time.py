# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """

        def find_minimum_start(schedule):
            min_start = float('inf')
            res = Interval()
            i = 0
            while i < len(schedule):
                if len(schedule[i]) == 0:
                    schedule.pop(i)
                    continue
                if min_start > schedule[i][0].start:
                    min_start = schedule[i][0].start
                    res = schedule[i][0]
                i += 1
            return res.start, res.end

        res = []
        prev_r = float('-inf')

        while schedule:

            l, r = find_minimum_start(schedule)
            res.append([prev_r, l])
            while True:
                still = False
                for intervals in schedule:
                    i = 0
                    while i < len(intervals):
                        if intervals[i].start > r:
                            break
                        else:
                            if r < intervals[i].end:
                                r = intervals[i].end
                                still = True
                            intervals.pop(i)
                if not still:
                    break
            prev_r = r

        return res[1:][:-1]

s = [[Interval(1,2), Interval(5,6)], [Interval(1,3)], [Interval(4,10)]]
s = [[Interval(1,3), Interval(6,7)], [Interval(2,4)], [Interval(2,5), Interval(9,12)]]
test = Solution()
print(test.employeeFreeTime(s))


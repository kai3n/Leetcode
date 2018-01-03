class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x:x[1])
        low, high, ans= -1, -1, 0
        for interval in intervals:
            if interval[0]>high:
                ans+=2
                low,high=interval[1]-1,interval[1]
            elif interval[0]>low:
                ans+=1
                low= high-1 if high==interval[1] else high
                high=interval[1]
        return ans
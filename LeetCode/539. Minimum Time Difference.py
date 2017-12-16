class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_slot = [0] * 24 * 60
        res = float('inf')
        for timePoint in timePoints:
            time_slot[int(timePoint[:2]) * 60 + int(timePoint[3:])] += 1
        time_slot += time_slot

        p1 = p2 = -1
        i = 0
        while i < len(time_slot):
            if time_slot[i] >= 2:
                return 0
            elif time_slot[i] == 1:
                if p2 == -1:
                    p2 = i
                else:
                    p1 = p2
                    p2 = i
                    res = min(((p2 - p1) + 1440) % 1440, ((p1 - p2) + 1440) % 1440, res)
            i += 1
        return res
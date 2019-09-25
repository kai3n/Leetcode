class HitCounter(object):
    def __init__(self):
        self.arr = []
        """
        Initialize your data structure here.
        """

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.arr.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for i in range(len(self.arr)):
            if timestamp - 300 < self.arr[i] <= timestamp:
                count += 1
        return count


class HitCounter(object):

    def __init__(self):
        self.q = [(0, 0)] * 300

    def hit(self, timestamp):
        idx = timestamp % 300
        time, hit = self.q[idx]
        if time != timestamp:
            self.q[idx] = timestamp, 1
        else:
            self.q[idx] = time, hit + 1

    def getHits(self, timestamp):
        ans = 0
        for i in xrange(0, len(self.q)):
            time, hit = self.q[i]
            if timestamp - time < 300:
                ans += hit
        return ans
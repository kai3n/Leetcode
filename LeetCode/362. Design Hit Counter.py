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
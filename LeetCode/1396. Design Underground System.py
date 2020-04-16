class UndergroundSystem(object):

    def __init__(self):
        self.in_dict = defaultdict(lambda: defaultdict(int))
        self.out_dict = defaultdict(lambda: defaultdict(int))

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.in_dict[stationName][id] = t

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.out_dict[stationName][id] = t

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        count = 0.0
        total = 0.0
        for station_id in self.in_dict[startStation]:
            if self.out_dict[endStation][station_id]:
                total += self.out_dict[endStation][station_id] - self.in_dict[startStation][station_id]
                count += 1
        return total / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
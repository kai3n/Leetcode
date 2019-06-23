class Solution(object):
    def carPooling(self, trips, capacity):
        locations = [[0, 0] for _ in range(1001)]
        for num_pass, src, dest in trips:
            locations[src][0] += num_pass
            locations[dest][1] += num_pass

        total = 0
        for i in range(len(locations)):
            total = total + locations[i][0] - locations[i][1]
            if total > capacity:
                return False
        return True
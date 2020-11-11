class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_degree = 30 * hour + 30 * minutes / 60
        minute_degree = 6 * minutes
        big = max(hour_degree, minute_degree)
        small = min(hour_degree, minute_degree)
        return min(big - small, 360 - big + small)

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0]*(n + 1)
        for i, j, k in bookings:
            res[i-1] += k
            res[j] -= k
        for i in range(1, len(res)):
            res[i] += res[i-1]
        return res[:-1]
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        distance = 0
        count = 0
        i = j = 0

        while i < len(seats):
            if seats[i]:
                break
            i += 1
        distance = max(distance, i)

        while j < len(seats):
            if seats[::-1][j]:
                break
            j += 1
        distance = max(distance, j)

        for i in range(len(seats)):
            if seats[i]:
                count = 0
            else:
                count += 1

            distance = max(distance, count // 2 + 1) if count % 2 else max(distance, round(count / 2))

        return int(distance)
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0
        r = len(people) - 1
        c = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                c += 1
            else:
                r -= 1
                c += 1
        return c
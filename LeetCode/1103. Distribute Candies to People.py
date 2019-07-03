class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        l = [0] * num_people
        i = 0
        while candies > i:
            l[i%num_people] += i+1
            candies = candies - i - 1
            i += 1
        l[i%num_people] += candies
        return l
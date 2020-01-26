class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        candidates = []
        for restaurant in restaurants:
            if veganFriendly and restaurant[2] != 1:
                continue
            if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                candidates.append([restaurant[0], restaurant[1]])
        candidates.sort(key=lambda x:[x[1], x[0]], reverse=True)
        candidates = [candidate[0] for candidate in candidates]
        return candidates
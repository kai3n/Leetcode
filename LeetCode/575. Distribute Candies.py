class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = dict()
        for i in candies:
            if d.get(i, 0) == 0:
                d[i] = 1
            else:
                d[i] += 1
        return len(d.items()) if len(d.items()) < len(candies)/2 else len(candies)//2

candies1 = [1, 1, 1, 1, 2, 2]
candies2 = [1, 1, 2, 3]
test = Solution()
print(test.distributeCandies(candies1))
print(test.distributeCandies(candies2))
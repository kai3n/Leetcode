class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if not flowerbed[i]:
                if not flowerbed[i - 1] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
        return True if n <= 0 else False

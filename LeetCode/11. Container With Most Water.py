# Brute Force Solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                maxWater = max(maxWater, min(height[j], height[i])*(j-i))
        return maxWater

# O(n) solution
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

test = Solution()
print(test.maxArea([1,1,3,5,6,1,10]))

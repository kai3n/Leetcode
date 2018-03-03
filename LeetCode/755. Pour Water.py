class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        while V > 0:
            left = K
            right = K
            target = K

            while 0 <= left - 1 and heights[left] >= heights[left - 1]:
                left -= 1
                if heights[target] > heights[left]:
                    target = left
            if target == K:
                while len(heights) - 1 >= right + 1 and heights[right] >= heights[right + 1]:
                    right += 1
                    if heights[target] > heights[right]:
                        target = right
            heights[target] += 1
            V -= 1
        return heights

test = Solution()
print(test.pourWater([3,1,3],5, 1))
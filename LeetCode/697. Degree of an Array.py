class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        ans = len(nums)
        degree = 0
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            if degree < count[x]:
                degree = count[x]
                ans = right[x] - left[x] + 1
            elif degree == count[x]:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
# class Solution:
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         stk = []
#         maxx = 0
#         heights.append(0)
#         for i in range(len(heights)):
#             while len(stk) > 0 and heights[i] < heights[stk[-1]]:
#                 s = stk.pop()
#                 if len(stk) == 0:
#                     maxx = max(maxx, i * heights[s])
#                 else:
#                     maxx = max(maxx, (i - stk[-1] - 1) * heights[s])
#             stk.append(i)
#         return maxx

class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):

            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans

s = Solution()
s.largestRectangleArea([1])
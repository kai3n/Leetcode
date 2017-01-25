# class Solution(object):
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         i = 0
#         while True:
#             if i*(i+1) <= n*2 < (i+1)*(i+2):
#                 return i
#             i += 1

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int((math.sqrt(1+8.0*n)-1)/2)

test = Solution()
print(test.arrangeCoins(0))
print(test.arrangeCoins(1))
print(test.arrangeCoins(5))
print(test.arrangeCoins(8))
print(test.arrangeCoins(1804289383))
print(test.arrangeCoins(1474612399))
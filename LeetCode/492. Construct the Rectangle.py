# # Memory Limit Exceeded
# class Solution(object):
#     def constructRectangle(self, area):
#         """
#         :type area: int
#         :rtype: List[int]
#         """
#         l = [area]
#         for n in range(area//2,0,-1):
#             if area % n == 0:
#                 l.append(n)
#         if len(l) % 2 == 1:
#             return [l[len(l)//2],l[len(l)//2]]
#         else:
#             return [l[(len(l)//2)-1],l[(len(l)//2)]]
#
# test = Solution()
# print(test.constructRectangle(1))
#
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        for n in range(int(math.ceil(math.sqrt(area)))+1,0,-1):
            if area % n == 0:
                if n**2 == area:
                    return [n,n]
                else:
                    return [max(n, area // n),min(n, area // n)]


test = Solution()
print(test.constructRectangle(134))





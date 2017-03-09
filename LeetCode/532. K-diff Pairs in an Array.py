# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         cnt = 0
#         d = dict()
#         if k < 0:
#             return 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]-nums[j] == k or nums[j]-nums[i] == k:
#                     if d.get((nums[i], nums[j]), 0) == 0 and d.get((nums[j], nums[i]), 0) == 0:
#
#                         d[(nums[i], nums[j])] = 1
#                         cnt += 1
#         return cnt
#
#
# input1 = [1, 1, 1, 2, 1]
# input2 = [1, 2, 3, 4, 5]
# input3 = [1, 3, 1, 5, 4]
# k1 = 1
# k2 = 1
# k3 = 0
#
# test = Solution()
# print(test.findPairs(input1, k1))
# print(test.findPairs(input2, k2))
# print(test.findPairs(input3, k3))

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) == 0:
            return 0

        count = 0
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        for key, value in map.items():
            if k == 0:
                if value >= 2:
                    count += 1
            else:
                if map.get(key+k, 0) != 0:
                    count += 1
        return count

input1 = [1, 1, 1, 2, 1]
input2 = [1, 2, 3, 4, 5]
input3 = [1, 3, 1, 5, 4]
k1 = 1
k2 = 1
k3 = 0

test = Solution()
print(test.findPairs(input1, k1))
print(test.findPairs(input2, k2))
print(test.findPairs(input3, k3))
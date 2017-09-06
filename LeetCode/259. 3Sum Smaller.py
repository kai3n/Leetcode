#Brute force solution
# class Solution(object):
#     def threeSumSmaller(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] < target:
#                         count += 1
#         return count

class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        return count

test = Solution()
print(test.threeSumSmaller([-2, 0, 1, 3], 2))


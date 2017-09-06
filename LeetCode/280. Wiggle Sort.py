#Brute Force Solution
# class Solution(object):
#     def wiggleSort(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             if i & 1:  # odd index
#                 j = nums[i:].index(max(nums[i:])) + i
#                 nums[i], nums[j] = nums[j], nums[i]
#             else:  # even index
#                 k = nums[i:].index(min(nums[i:])) + i
#                 nums[i], nums[k] = nums[k], nums[i]
#         return nums

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if (i & 1) ^ (nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums


test = Solution()
print(test.wiggleSort([3, 5, 2, 1, 6, 4]))
print(test.wiggleSort([1, 2, 3]))
print(test.wiggleSort([9,6,2,2,9]))
print(test.wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2]))
print(test.wiggleSort([1,1,1,1,1,2,2,2,2,2]))
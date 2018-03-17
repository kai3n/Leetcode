class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = [num for num in nums]
        nums2 = [num for num in nums]
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums1[i - 1] = nums1[i]
                nums2[i] = nums[i - 1]
                break

        print(nums2)
        c1 = c2 = True
        for i in range(1, len(nums)):
            if nums1[i - 1] > nums1[i]:
                c1 = False
            if nums2[i - 1] > nums2[i]:
                c2 = False

        return c1 or c2

nums = [2,3,3,2,4]

test = Solution()
print(test.checkPossibility(nums))


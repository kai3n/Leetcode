class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        c0 = c1 = c2 = 0

        for num in nums:
            if num == 0:
                c0 += 1
            if num == 1:
                c1 += 1
            if num == 2:
                c2 += 1

        i = 0
        while i < c0:
            nums[i] = 0
            i += 1
        while i < c0 + c1:
            nums[i] = 1
            i += 1
        while i < c0 + c1 + c2:
            nums[i] = 2
            i += 1



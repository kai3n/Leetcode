class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(a, i):
            for j in range(len(a)-1, i, -1):
                if a[j] > a[i]:
                    a[j], a[i] = a[i], a[j]
                    break
        def reverse(a, i):
            first = i
            last = len(a)-1
            while first < last:
                a[first], a[last] = a[last], a[first]
                first += 1
                last -= 1

        if len(nums) <= 1:
            return

        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i
                break

        if index != 0:
            swap(nums, index-1)
        reverse(nums, index)




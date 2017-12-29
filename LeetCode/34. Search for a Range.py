class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def find_start_index(nums, target, flag=True):
            first = 0
            last = len(nums) - 1
            while first <= last:
                mid = (first + last) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
            return first if flag else last

        idx = find_start_index(nums, target)
        if idx < 0 or idx >= len(nums):
            return [-1, -1]
        if nums[idx] == target:
            start_idx = find_start_index(nums, target - 0.1, True)
            finish_idx = find_start_index(nums, target + 0.1, False)
            return [start_idx, finish_idx]
        else:
            return [-1, -1]

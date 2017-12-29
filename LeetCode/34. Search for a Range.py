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



"""
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

"""
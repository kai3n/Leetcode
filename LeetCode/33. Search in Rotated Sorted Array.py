class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        pivot = self.findPivot(nums)
        if target >= nums[0] and pivot != 0:
            return self.binarySearch(nums, 0, pivot-1, target)
        else:
            return self.binarySearch(nums, pivot, len(nums)-1, target)

    def findPivot(self, nums):
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < nums[mid-1]:
                return mid
            elif nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid - 1
        return mid

    def binarySearch(self, nums, first, last, target):

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return -1

arr = [4, 5, 6, 7, 0, 1, 2]
arr = [1,3]
test= Solution()
print(test.search(arr, 1))

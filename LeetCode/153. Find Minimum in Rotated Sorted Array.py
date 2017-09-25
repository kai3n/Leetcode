class Solution(object):
    def findMin(self, nums):
        first = 0
        last = len(nums) - 1

        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid - 1
        return


a = [4, 5, 6, 7, 0, 1, 2]
b = [2, 1]
c = [1]
test = Solution()
print(test.findMin(a))
print(test.findMin(b))
print(test.findMin(c))
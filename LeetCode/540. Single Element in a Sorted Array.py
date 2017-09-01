class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = len(nums)-1

        while first <= last:
            mid = (first + last) // 2
            if last - first == 2:
                return nums[first] ^ nums[first+1] ^ nums[first+2]
            if mid % 2 == 1:
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
                elif nums[mid] == nums[mid-1]:
                    first = mid+1
                else:
                    last = mid-1
            else:
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
                elif nums[mid] == nums[mid+1]:
                    first = mid + 2
                else:
                    last = mid - 2

test = Solution()
print(test.singleNonDuplicate([1,1,2]))
print(test.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(test.singleNonDuplicate([3,3,7,7,10,11,11]))



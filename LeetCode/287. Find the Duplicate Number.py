class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow = nums[0]
        fast = nums[nums[0]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0;
        while (fast != slow):
            fast = nums[fast]
            slow = nums[slow]

        return slow


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low
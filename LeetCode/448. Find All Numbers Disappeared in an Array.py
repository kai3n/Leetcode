class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(len(nums)):
            nums[(nums[i]-1) % len(nums)] += len(nums)
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                res.append(i+1)
        return res

nums = [4,3,2,7,8,2,3,1]
test = Solution()
print(test.findDisappearedNumbers(nums))
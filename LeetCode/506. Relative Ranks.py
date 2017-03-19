class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        sortedNums = sorted(nums, reverse=True)

        count = 1
        for j in sortedNums:
            if count == 1:
                nums[d[j]] = "Gold Medal"
            elif count == 2:
                nums[d[j]] = "Silver Medal"
            elif count == 3:
                nums[d[j]] = "Bronze Medal"
            else:
                nums[d[j]] = str(count)
            count += 1
        return nums

test = Solution()
print(test.findRelativeRanks([5,4,3,2,1]))
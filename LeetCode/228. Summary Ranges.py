class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        nums.append(-1)
        begin = end = 0

        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                end = i + 1
            else:
                if begin != end:
                    res.append("{}->{}".format(nums[begin], nums[end]))
                else:
                    res.append("{}".format(nums[begin]))
                begin = i + 1
                end = i + 1
        return res

nums = [0, 1, 2, 4, 5, 7, 10]

test = Solution()
print(test.summaryRanges(nums))


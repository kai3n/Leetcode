class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numDict = dict()
        for num in nums:
            if numDict.get(num) is None:
                numDict[num] = 1
            else:
                numDict[num] += 1

        retList = list()
        for key, value in numDict.items():
            if value == 1:
                retList.append(key)
        return retList



test = Solution()
print(test.singleNumber([1,2,1,3,2,5]))


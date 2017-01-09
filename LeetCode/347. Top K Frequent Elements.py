class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numDic = dict()

        for num in nums:
            if numDic.get(num) is None:
                numDic[num] = 1
            else:
                numDic[num] += 1
        numDic = sorted(numDic,key=numDic.get, reverse=True)
        return numDic[:k]

test = Solution()
print(test.topKFrequent([4,4,4,2,2,5],3))

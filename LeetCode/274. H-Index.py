class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        hIndex = 0
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                hIndex = i+1
        return hIndex

citations = [3, 0, 6, 1, 5]

test = Solution()
print(test.hIndex(citations))


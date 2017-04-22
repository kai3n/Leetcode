class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= n-mid:
                r = mid-1
            else:
                l = mid+1
        return n-l


citations = [0, 1, 2, 3, 5, 6]
citations2 = [1]
citations3 = [0, 1]


test = Solution()
print(test.hIndex(citations))
#print(test.hIndex(citations2))
#print(test.hIndex(citations3))


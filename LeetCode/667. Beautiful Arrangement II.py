class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        j = k+1
        l = 1
        for i in range(1, k+2):
            if i % 2 == 1:
                res.append(l)
                l += 1
            else:
                res.append(j)
                j -= 1
        for i in range(len(res)+1, n+1):
            res.append(i)
        return res
    '''
    def constructArray(self, n, k):
        a = range(1, n + 1)
        for i in range(1, k):
            a[i:] = a[:i - 1:-1]
        return a
    '''

test= Solution()
print(test.constructArray(3, 2))
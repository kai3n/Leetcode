class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        memo = {1:0}
        def transform(num):
            if num in memo:
                return memo[num]
            if num & 1:
                res = transform(3*num+1)
                memo[num] = res + 1
                return memo[num]
            else:
                res = transform(num/2)
                memo[num] = res + 1
                return memo[num]
        return sorted(range(lo, hi+1), key=transform)[k-1] 

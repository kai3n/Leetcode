class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(nums)
        keys = sorted(count)
        for n in keys:
            if count[n] > 0:
                minus = count[n]
                for i in range(n, n + k):
                    if count[i] < minus:
                        return False
                    count[i] -= minus
        return True
        

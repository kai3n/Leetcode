class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        d = {0: -1}
        total = 0
        lsize = float('inf')
        result = float('inf')
        for i in range(len(arr)):
            total += arr[i]
            d[total] = i
            
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            if d.get(total - target) is not None:
                lsize = min(lsize, i - d.get(total - target))
            if d.get(total + target) is not None and lsize < float('inf'):
                result = min(result, d.get(total + target) - i + lsize)
        return result if result != float('inf') else -1
                

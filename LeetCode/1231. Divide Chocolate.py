class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        def divide(target):
            total, count = 0, 0
            for element in sweetness:
                total += element
                if total >= target:
                    count += 1
                    total = 0
            return count
        lo, hi = min(sweetness), sum(sweetness)//(K + 1)
        while lo < hi:
            target = (lo + hi + 1)//2
            if divide(target) < K + 1:
                hi = target - 1
            else:
                lo = target
        return hi
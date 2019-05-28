class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        beg = end = 0
        s = 0
        grumpy_max = 0
        while end < len(customers):
            while end < len(customers) and end - beg < X:
                if grumpy[end]:
                    s += customers[end]
                end += 1
            grumpy_max = max(grumpy_max, s)
            if end == len(customers):
                break
            if grumpy[beg]:
                s -= customers[beg]
            beg += 1

        ungrumpy_sum = sum(customers[i] if grumpy[i] == 0 else 0 for i in range(len(customers)))
        return ungrumpy_sum + grumpy_max

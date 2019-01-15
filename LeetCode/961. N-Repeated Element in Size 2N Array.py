class Solution(object):
    def repeatedNTimes(self, A):
        from collections import Counter
        count = Counter(A)
        for k in count:
            if count[k] > 1:
                return k
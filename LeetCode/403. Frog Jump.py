class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        d = defaultdict(list)
        s = set(stones)
        d[0].append(0)
        for i in range(len(stones)):
            for k in d[stones[i]]:
                for step in [k-1, k, k+1]:
                    if step > 0 and stones[i] + step in s:
                        d[stones[i] + step].append(step)
        return len(d[stones[-1]]) > 0
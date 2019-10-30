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


class Solution(object):
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        # dfs
        candidate = [speed - 1, speed, speed + 1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False
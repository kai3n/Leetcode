class Solution:
    def numPairsDivisibleBy60(self, time):
        from collections import defaultdict

        d = defaultdict(int)
        res = 0
        for i in range(len(time)):
            d[time[i]%60] += 1
        for k, v in d.items():
            if k == 30 or k == 0:
                res += v*(v-1)/2
            elif d.get(60-k) is not None:
                res += d.get(60-k)*v/2
        return int(res)
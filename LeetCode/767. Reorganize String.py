class Solution:
    def reorganizeString(self, S):
        a = sorted(sorted(S), key=S.count)
        h = len(a) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])

#priority queue solution
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        res = ""
        pq = []
        c = Counter(S)
        for key, value in c.items():
            heapq.heappush(pq, (-value, key))
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += b
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(res) != len(S): return ""
        return res
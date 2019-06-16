class Solution(object):
    def highFive(self, items):
        d = collections.defaultdict(list)

        for idx, val in items:
            heapq.heappush(d[idx], val)

            if len(d[idx]) > 5:
                heapq.heappop(d[idx])

        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]

        return res
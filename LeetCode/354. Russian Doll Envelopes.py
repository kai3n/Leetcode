class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        new_list = []
        for envelope in envelopes:
            if envelope not in new_list:
                new_list.append(envelope)
        envelopes = new_list
        envelopes.sort()
        dp = [1]*len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


from bisect import bisect_left

class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        max_idx = 0
        heights = [envelopes[0][1]] + [0] * (len(envelopes) - 1)
        for e in envelopes:
            idx = bisect_left(heights, e[1], hi=max_idx + 1)
            heights[idx] = e[1]
            max_idx = max(max_idx, idx)
        return max_idx + 1
class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        counts = collections.defaultdict(int)
        vl = sorted(zip(values,labels))
        ans = 0
        while num_wanted and vl:
            val, lab = vl.pop()
            if counts[lab] < use_limit:
                ans += val
                counts[lab] += 1
                num_wanted -= 1
        return ans
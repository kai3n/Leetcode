class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        i = res = 0
        j = 1
        while j < len(s):
            if s[i] == s[j]:
                while j < len(s) and s[i] == s[j]:
                    j += 1
                res += sum(cost[i:j]) - max(cost[i:j])
                i = j
                j = i + 1
            else:
                i += 1
                j = i + 1
        return res
        

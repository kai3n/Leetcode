class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if len(rating) < 3:
            return 0
        res = 0
        greater = defaultdict(int)
        less = defaultdict(int)
        
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                elif rating[j] < rating[i]:
                    less[i] += 1
        
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                if rating[j] > rating[i]:
                    res += greater[j]
                elif rating[j] < rating[i]:
                    res += less[j]
        return res

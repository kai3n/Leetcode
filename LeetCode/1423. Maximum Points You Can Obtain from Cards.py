class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if not cardPoints:
            return 0
        total = sum(cardPoints)
        total_list = [cardPoints[0]]
        
        for i in range(1, len(cardPoints)):
            total_list.append(total_list[-1] + cardPoints[i])
        
        min_val = float('inf')
        j = len(cardPoints) - k
        for i in range(len(cardPoints) - j + 1):
            if i == 0:
                min_val = min(min_val, total_list[i + j - 1])
            else:
                min_val = min(min_val, total_list[i + j - 1] - total_list[i - 1])
        return total - min_val
                

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        for v1, v2 in zip(heights, sorted(heights)):
            if v1 != v2:
                count += 1
        return count
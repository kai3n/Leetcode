class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec2[3] <= rec1[1] or rec1[3] <= rec2[1]:
            return False
        elif rec2[2] <= rec1[0] or rec1[2] <= rec2[0]:
            return False
        return True
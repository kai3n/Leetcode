class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """

        clips.sort()
        i = 0
        count = 1
        try:
            end = max([x[1] for x in clips if x[0] == 0])
            if end >= T:
                return count
        except:
            return -1
        while i < len(clips):
            new_end = clips[i][1]
            f = False
            while i < len(clips) and clips[i][0] <= end:
                new_end = max(new_end, clips[i][1])
                i += 1
                f = True
            count += 1
            end = new_end
            if end >= T:
                return count
            if not f:
                i += 1
        return -1
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        idx2char = [-1] * len(s)
        for i, j in enumerate(indices):
            idx2char[j] = s[i]
        return "".join(idx2char)

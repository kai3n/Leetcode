class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        for c in sorted(set(text)):
            suffix = text[text.index(c):]
            if set(suffix) == set(text):
                return c + self.smallestSubsequence(suffix.replace(c, ''))
        return ''
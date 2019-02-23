class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """

        def flip(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        flip(str, 0, len(str) - 1)
        beg = 0
        end = 0
        while end < len(str):
            if str[end] == " ":
                flip(str, beg, end - 1)
                beg = end + 1
            end += 1
        flip(str, beg, end - 1)
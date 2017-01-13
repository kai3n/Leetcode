class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list()
        r = ""
        for i in s.split():
            slist.append(i)
        while len(slist) != 0:
            if len(slist) == 1:
                r += slist.pop()
            else:
                r += slist.pop() + " "
        return r

test = Solution()
print(test.reverseWords('the sky is blue'))
print(test.reverseWords('    '))

"""
def reverseWords(self, s):
    return " ".join(s.strip().split()[::-1])
"""
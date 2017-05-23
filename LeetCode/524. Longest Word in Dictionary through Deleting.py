class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for w in d:
            i = 0
            for c in s:
                if i < len(w) and w[i] == c:
                    i += 1
            if i == len(w):
                return w
        return ""

test = Solution()
print(test.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
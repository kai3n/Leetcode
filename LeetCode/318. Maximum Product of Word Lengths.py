# time limit code
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = list()
        for i in range(len(words)):
            for j in range(len(words)):
                s1 = set(words[i])
                s2 = set(words[j])
                intersectLen = len(s1.intersection(s2))
                if intersectLen == 0:
                    l.append(len(words[i])*len(words[j]))
        if len(l) != 0:
            return max(l)
        else:
            return 0
test = Solution()
print(test.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(test.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(test.maxProduct(["a", "aa", "aaa", "aaaa"]))
print(test.maxProduct(["a", "ab", "ac"]))
print(test.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
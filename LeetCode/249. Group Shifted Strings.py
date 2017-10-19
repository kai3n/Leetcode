class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = dict(list())
        res = []
        for string in strings:
            f = False
            for i in range(26):
                s = ""
                for l in string:
                    s += chr(ord(l)+i) if ord(l)+i <= 122 else chr(ord(l)+i - 26)
                if d.get(s, None) != None:
                    d[s] += [string]
                    f = True
            if not f:
                d[string] = [string]
        for v in d.values():
            res.append(v)
        return res



strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

test = Solution()
print(test.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.res = []
        def helper(s, word):
            if not s:
                self.res.append(word)
            else:
                if s[0] == "{":
                    i = s.find("}")
                    for letter in s[1:i].split(','):
                        helper(s[i+1:], word+letter)
                else:
                    helper(s[1:], word + s[0])
        helper(S, "")
        self.res.sort()
        return self.res
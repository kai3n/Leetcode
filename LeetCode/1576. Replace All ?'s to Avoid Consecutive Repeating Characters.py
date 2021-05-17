class Solution:
    def modifyString(self, s: str) -> str:
        s = list('#' + s + '#')
        for i in range(len(s)):
            if s[i] == '?':
                for x in 'abc':
                    if s[i-1] != x != s[i+1]:
                        s[i] = x
                        break
        return ''.join(s[1:-1])

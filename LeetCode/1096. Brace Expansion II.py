import itertools

class Solution:
    def braceExpansionII(self, expression):
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append(c)
        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        return sorted(word_set)

s = Solution()
e = "{a,b}{c,{d,e}}"
e = "{{a,z},a{b,c},{ab,z}}"
print(s.braceExpansionII(e))

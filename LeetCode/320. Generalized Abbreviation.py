def helper(word):
    if len(word) == 1:
        return [word[-1], "1"]
    else:
        pre = helper(word[1:])
    res = []
    for i in (word[0], "1"):
        for p in pre:
            if i.isdigit() and p[0].isdigit():
                j = 0
                while j < len(p) and p[j].isdigit():
                    j += 1
                res.append(str(int(i) + int(p[:j])) + p[j:])
            else:
                res.append(i + p)
    return res

class Solution(object):
    def generateAbbreviations(self, word):
        if not word:
            return [""]
        res = helper(word)

        return res

word = "interaction"
test = Solution()
print(test.generateAbbreviations(word))
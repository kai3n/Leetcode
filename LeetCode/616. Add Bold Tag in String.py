class Solution(object):
    def addBoldTag(self, S, A):
        paint = [False] * len(S)
        for i in range(len(S)):
            block = S[i:]
            for word in A:
                if block.startswith(word):
                    paint[i:i + len(word)] = [True] * len(word)

        ans = []
        for i, u in enumerate(S):
            if paint[i] and (i == 0 or not paint[i - 1]):
                ans.append('<b>')
            ans.append(u)
            if paint[i] and (i == len(S) - 1 or not paint[i + 1]):
                ans.append('</b>')

        return "".join(ans)


# "<b>abc</b>xyz<b>123</b>"

s = "abcxyz123"
dict = ["abc","123"]

# "<b>aaabbc</b>c"
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
#
# s = "aaabbcc"
# dict = ["aaa","aab","bc","aaabbcc"]

# s = "aaabbcc"
# dict = ["a","b","c"]

s = "abcdef"
dict = ["ab","bc","cd","de","ef","fg","gh"]
test = Solution()
print(test.addBoldTag(s, dict))
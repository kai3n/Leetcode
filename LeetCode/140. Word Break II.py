# Time limit Solution
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []

        def dfs(s, p):
            if not s:
                res.append(' '.join(p))
            else:
                for i in range(len(s)):
                    if s[:i + 1] in wordDict:
                        dfs(s[i + 1:], p + [s[:i + 1]])

        dfs(s, [])
        return res

# Memoization
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

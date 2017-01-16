class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        wordList = str.split()
        letterDict = dict()
        wordDict = dict()
        for i, letter in enumerate(pattern):
            if letterDict.get(letter) == None:
                letterDict[letter] = wordList[i]
            else:
                if letterDict[letter] != wordList[i]:
                    return False

        for i, word in enumerate(wordList):
            if wordDict.get(word) == None:
                wordDict[word] = pattern[i]
            else:
                if wordDict[word] != pattern[i]:
                    return False

        return True

test = Solution()
print(test.wordPattern("abba","dog cat cat dog"))
print(test.wordPattern("abba","dog cat cat fish"))
print(test.wordPattern("aaaa","dog cat cat dog"))
print(test.wordPattern("abba","dog dog dog dog"))
print(test.wordPattern("aaa","aa aa aa aa"))
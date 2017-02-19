class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower() or (word[0] == word[0].upper() and word[1:] == word[1:].lower()):
            return True
        return False

test = Solution()
print(test.detectCapitalUse('UsdfsS'))


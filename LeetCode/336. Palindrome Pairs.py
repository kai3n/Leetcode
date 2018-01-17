# Time limit solution
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        cache = {}
        def is_palindrome(word1, word2):
            return word1 + word2 == (word1 + word2)[::-1]
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and is_palindrome(words[i], words[j]):
                    res.append([i, j])
        return res

# Time limit solution O(n*n*k)
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

    # Accepted Solution O(n*k*k)
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.iteritems():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        min_len = float('inf')
        min_word = ''
        d1 = collections.defaultdict(int)
        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                d1[licensePlate[i].lower()] += 1
        print(d1)
        for word in words:
            d2 = collections.defaultdict(int)
            for w in word:
                d2[w.lower()] += 1
            f = True
            for k, v in d1.items():
                if d2[k] < d1[k]:
                    f = False
            if f:
                if min_len > len(word):
                    min_len = len(word)
                    min_word = word
        return min_word